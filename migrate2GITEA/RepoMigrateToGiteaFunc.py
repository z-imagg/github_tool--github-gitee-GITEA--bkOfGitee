#!/usr/bin/env python
# -*- coding: <encoding name> -*-

# 【文件作用】 迁移给定git仓库url到gitea服务
# 【术语】 orn == origin == 源头,  frm==from , mgr == migrate == 迁移,   RUrl == RepoUrl == git仓库Url
# 【大背景】 github仓库  ----import导入--->  镜像gitee仓库  ----migrate迁移---> 本地GITEA仓库 
# 【术语】在迁移语境下：  orn源头 指的是 github仓库 , frm来自 值的是 镜像gitee仓库,  目标 指的是 本地GITEA仓库
# 【术语】 toLcRUrl == toLocalRepoUrl == "目标即本地仓库"的仓库Url
import sys

sys.path.append("/app/github-gitee-GITEA/py_util/")

from pathlib import Path
import re
import git

from GitPyUtil import checkRepoByClone
from gitea_api_cfg import api_base_url, api_token
import httpx
import typing


from httpx_util import httpx_post_json

from GitRepoUrlParser import GitRepoUrlC, gitMirrorRepoUrlParseF,gitRepoUrlParseF,_GIT
from gitea_api_cfg import api_base_url,gitea_migrate_api_timeout_seconds
from global_var import getGlbVarInst
import httpcore
import traceback

def giteaMigrateApi(ornRUrl:str,frmBaseUrl:str,frmOrg:str)->typing.Tuple[bool,GitRepoUrlC,str]:
  ornRUrlO=gitRepoUrlParseF(ornRUrl)

  #将 原始仓库url(==github仓库url) 通过 镜像信息(==frm*) 转为 镜像仓库url。 镜像==gitee
  frmRUrlO=ornRUrlO.to_mirror_url(frmBaseUrl,frmOrg)
  frmRUrl:str = frmRUrlO.url_str()

  #构造本地GITEA仓库url
  toLcRUrl=f"{api_base_url}/{ornRUrlO.orgName}/{ornRUrlO.repoName}{_GIT}"

  mgr_desc=f"原始仓库【{ornRUrl}】 ；迁移内容【{frmRUrl}】--->【{toLcRUrl}】"    ;  

  try:
    if checkRepoByClone(toLcRUrl,"检目的仓") is not None:
      #返回 迁移结果、镜像仓库url、本地GITEA仓库url
      print(f"目的仓已有，无需迁移接口; 『 {mgr_desc}』 ")
      return (True,frmRUrlO,toLcRUrl)
  except git.GitCommandError as e:
    print(f"目的仓尚无， 继续迁移接口")
  
  #迁移之前检查 检查gitee镜像仓库是否能正常克隆
  checkRepoByClone(frmRUrl,"检查源")

  """ #本地GITEA创建组织接口 例子
  curl -X 'POST' \
  'https://github.local/api/v1/orgs?token=ab2a90dc37210a4f9aee91ab959bfa3fc1f6ba6a' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "username": "NVlabs",
  "repo_admin_change_team_access": true,
  "visibility": "public"
}'
"""
  #构造 本地GITEA创建组织接口 请求
  apiUrl_newOrg=f'{api_base_url}/api/v1/orgs?token={api_token}'
  reqBdy_newOrg={
    "username": ornRUrlO.orgName,
  }
  #调用本地GITEA服务的创建组织接口
  resp_newOrg=httpx_post_json(apiUrl=apiUrl_newOrg,reqBodyDct=reqBdy_newOrg )
  #判定接口执行结果
  ok_newOrg=resp_newOrg.status_code==422 or resp_newOrg.is_success #422 gitea 已经存在组织
  #打印提示消息
  msg_newOrg=f'{"创建GITEA组织成功" if resp_newOrg else "创建GITEA组织失败" }，【{resp_newOrg.status_code}, {resp_newOrg.text}】'  ; print(msg_newOrg)
  #若创建本地GITEA组织失败，只能终止了。
  if(not ok_newOrg):
    #返回 迁移结果、镜像仓库url、本地GITEA仓库url
    return (False,None,None)
  

  """ #本地GITEA迁移仓库接口 例子
  curl -k -X 'POST' \
    'https://github.local/api/v1/repos/migrate?token=b1d490eaf6b88a6c37bd482d8e05e3a0061f066c' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{
    "clone_addr": "https://gitee.com/mirrr/NVlabs--cub.git",
    "repo_name": "cub",
    "repo_owner": "NVlabs"
  }'

  """

  #构造 本地GITEA迁移仓库接口 请求
  apiUrl_migrate=f'{api_base_url}/api/v1/repos/migrate?token={api_token}'
  reqBdy_migrate={
      "clone_addr": frmRUrl,
    "repo_owner": ornRUrlO.orgName,
    "repo_name": ornRUrlO.repoName
  }

  mgr_msg=f"迁移接口开始... ; {mgr_desc}"  ;  print(mgr_msg)

  ok_mgr:bool=None
  try:
    #调用本地GITEA服务的迁移接口
    resp_mgr=httpx_post_json(apiUrl=apiUrl_migrate,reqBodyDct=reqBdy_migrate,timeoutSecs=gitea_migrate_api_timeout_seconds)
    #判定接口执行结果
    ok_mgr= resp_mgr.status_code == 409 or resp_mgr.is_success #409 gitea 已经存在仓库
    ok_mgr_desc=f'{"迁移接口成功" if ok_mgr else "迁移接口失败" }'  ; 
  except (httpcore.ReadTimeout | httpx.ReadTimeout)as htE:
    print(f"本地GITEA服务响应超时，结果未知，正常返回。下一步的loop_clone_wait_F可以应付。")
    traceback.print_exception(htE)
    #返回 迁移结果、镜像仓库url、本地GITEA仓库url
    return (True,frmRUrlO,toLcRUrl)
  #打印提示消息
  resp_mgr_desc=f"【GITEA迁移接口响应】状态码【{resp_mgr.status_code}】 "   ;  msg_mgr=f'{ok_mgr_desc};   {resp_mgr_desc}'   ; print(msg_mgr)

  #返回 迁移结果、镜像仓库url、本地GITEA仓库url
  return (ok_mgr,frmRUrlO,toLcRUrl)