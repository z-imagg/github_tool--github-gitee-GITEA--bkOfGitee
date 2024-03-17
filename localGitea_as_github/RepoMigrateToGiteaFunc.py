#!/usr/bin/env python
# -*- coding: <encoding name> -*-

# 【文件作用】 迁移给定git仓库url到gitea服务

from pathlib import Path
import re

from gitea_api_cfg import api_base_url, api_token
import httpx
import typing

import sys
sys.path.append("/fridaAnlzAp/github-gitee-gitea/py_util/")

from GitRepoUrlParser import GitRepoUrlC, gitMirrorRepoUrlParseF,gitRepoUrlParseF,_GIT
from gitea_api_cfg import api_base_url,gitea_migrate_api_timeout_seconds

def giteaMigrateApi(ornRUrl:str,mrrBaseUrl:str,mrrOrg:str)->typing.Tuple[bool,GitRepoUrlC,str]:
  ornRUrlO=gitRepoUrlParseF(ornRUrl)

  """
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

  apiUrl_newOrg=f'{api_base_url}/api/v1/orgs?token={api_token}'
  reqBdy_newOrg={
    "username": ornRUrlO.orgName,
  }
  resp_newOrg=httpx.post(url=apiUrl_newOrg,json=reqBdy_newOrg,verify=False)
  ok_newOrg=resp_newOrg.status_code==422 or resp_newOrg.is_success #422 gitea 已经存在组织
  msg_newOrg=f'{"创建gitea组织成功" if resp_newOrg else "创建gitea组织失败" }，【{resp_newOrg.status_code}, {resp_newOrg.text}】'
  print(msg_newOrg)
  if(not ok_newOrg):
    return (False,None)
  
  

  """
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

  mrrRUrlO=ornRUrlO.to_mirror_url(mrrBaseUrl,mrrOrg)
  mirrRUrl:str = mrrRUrlO.url_str()
  apiUrl_migrate=f'{api_base_url}/api/v1/repos/migrate?token={api_token}'
  reqBdy_migrate={
      "clone_addr": mirrRUrl,
    "repo_owner": ornRUrlO.orgName,
    "repo_name": ornRUrlO.repoName
  }
  localRUrl=f"{api_base_url}/{ornRUrlO.orgName}/{ornRUrlO.repoName}{_GIT}"
  mgr_desc=f"原始仓库【{ornRUrl}】 ；迁移内容【{mirrRUrl}】--->【{localRUrl}】"
  mgr_msg=f"正在迁移...，耗时取决于仓库大小; {mgr_desc}"
  print(mgr_msg)
  resp_mgr=httpx.post(url=apiUrl_migrate,json=reqBdy_migrate,verify=False,timeout=gitea_migrate_api_timeout_seconds)
  resp_mgr_desc=f"【gitea迁移接口响应】状态码【{resp_mgr.status_code}】，响应文本【{resp_mgr.text}】"
  ok_mgr= resp_mgr.status_code == 409 or resp_mgr.is_success #409 gitea 已经存在仓库
  ok_mgr_desc=f'{"迁移成功" if ok_mgr else "迁移失败" }'
  msg_mgr=f'{ok_mgr_desc}; {mgr_desc}; \n {resp_mgr_desc}'
  print(msg_mgr)
  return (ok_mgr,mrrRUrlO,localRUrl)