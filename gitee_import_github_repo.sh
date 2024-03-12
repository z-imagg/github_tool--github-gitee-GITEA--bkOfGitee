#!/usr/bin/env bash

#【文件作用】 gitee页面的 异步导入给定url仓库接口 使用步骤
#【文件内容概述】
#   1、2、3： 找出接口、分析接口
#   4：给出接口使用步骤

#术语： 异步导入给定url仓库接口 == 导入给定url接口 == 接口
#术语:  接口的curl例子 == 接口例子,  '<--' 为 覆盖（赋值）操作

#1. 人工导入给定url仓库
#gitee从URL导入：   https://gitee.com/projects/import/url
#  Git仓库Url: https://github.com/NVlabs/cub.git
#  仓库名称: NVlabs--cub
#  归属: mirrr
#  路径: NVlabs--cub
#  仓库介绍: 导入github仓库NVlabs/cub
#  开源: 勾选
#  私有: 不勾选
#  选择语言: (不动，保持原样,即为)请选择语言
#  点击“导入”按钮
#此为人工正常导入 给定url仓库 的操作

#2. 找到 步骤1 中 导入给定url 的 实际接口 
#通过firefox开发者工具 发现:  "POST 请求 https://gitee.com/mirrr/projects" 即为 导入给定url的接口
# 确认步骤:
#    2.0  firefix 新页面打开 刚刚导入的项目 https://gitee.com/mirrr/NVlabs--cub.git，正常删除   
#    2.1. 点击 "firefox开发者工具.右上放.齿轮" --> 选择 "持续记录"
#    2.2. 在 "firefox开发者工具.网络" 找到该请求 --> 右击 该请求 --> 点击 "重发"，  即 原样回放该请求（即导入给定url请求）
#    2.3. firefix 新页面打开 https://gitee.com/mirrr/NVlabs--cub.git，确实有

#3. 步骤2 中 导入给定url接口 请求记录
#     续航符是手工加的，方便阅读
curl 'https://gitee.com/mirrr/projects' --compressed -X POST \
-H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0' \
-H 'Accept: text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01' \
-H 'Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2' \
-H 'Accept-Encoding: gzip, deflate, br' \
-H 'Referer: https://gitee.com/projects/import/url' \
-H 'X-CSRF-Token: zKv+8najDxCg4D4YMZhi/FRylRNk1Wq3uVjuKFmMuDDfks9igb1z0HnUDiebGd7itIh1iZanKkcUomLBIN9YaA==' \
-H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' \
-H 'X-Requested-With: XMLHttpRequest' \
-H 'Origin: https://gitee.com' \
-H 'Connection: keep-alive' \
-H 'Cookie: sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221895999%22%2C%22first_id%22%3A%2218e2b2e2deee02-0ed4ffee05327f8-47380724-2073600-18e2b2e2defc0c%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMThlMTczNjU2MWMyOGUtMDdhMGQ1ODI0ODU3MTctNDczODA3MjQtMjA3MzYwMC0xOGUxNzM2NTYxZDZjNSIsIiRpZGVudGl0eV9sb2dpbl9pZCI6IjE4OTU5OTkifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%221895999%22%7D%2C%22%24device_id%22%3A%2218e1736561c28e-07a0d582485717-47380724-2073600-18e1736561d6c5%22%7D; sensorsdata2015jssdkchannel=%7B%22prop%22%3A%7B%22_sa_channel_landing_url%22%3A%22%22%7D%7D; user_locale=zh-CN; oschina_new_user=false; Hm_lvt_24f17767262929947cc3631f99bfd274=1709941077,1709946541,1710038395,1710121431; remote_way=ssh; visit-gitee--2024-03-06=1; yp_riddler_id=75f1f438-d58b-47c2-92a2-e0c4ee6b3674; slide_id=10; BEC=1f1759df3ccd099821dcf0da6feb0357; gitee-session-n=SEFCNjlubWNDNE5sbmVzck1ndmVwUTFyN2g2T1NBNFUrOTF6cU1FY0NqYkJTTEJiMC8yRjZxd1ZGVDROOVhndlFGeTJXd0IyY1dFYnltdGtUYStoQ3VZZjBoNkZ2cXNWWTNGb294NzVmTXZGRGtQMmRoN29LUUl5SFd2SzRIWjFUWEpjQWx0blFTSGpsd3cyWUpnYWt0c3ZiM0tQUGRFY3B6WmdmeXFFYTVUc25zbHdRK1U0NTdEYTJCQVRBb3RCT2V0MHZMdkgxVUwvc2I0cFFJZmIrcy9PMjFXd29RSHRYVUd0eDBzL0JnaWlaU0F4TmMvd0Q1ZDdQSjA0U2RRQVRmb2xvMGJ4VHVhRmYyTkhzSkZPNW1YRnhabTAxcVF0SFV3bVM5azVOVThrMUJUZHdrbHZTc0R0MW92YVlvZG1LTlZ4MDZub3hIWGF2TDI3NkhKYmNKbklLY1o4K0V6Q1B6L3h2eVVhYllEaytRTDQwMVhKVFVNeFcxbVhOdnVTTzZTVnlvcUlPRmlIODZJL3pwZ2Y4OVR0WC8zZWRiUW52N1dzNHFyQUxsWmVKcjBvRHVtVWd3VEk4dFVjTWJ2U3QwNXlZdU1XcXU4eEswZFY3ZlljdS9TQjRRYTYvTHJ1TkxvZWVwZVJIa1lSS0FlTzFVVGdycVRqUFFPeUhlRkl3N1FSTlo1RXRMWTlmWTR3aVhIWXgzQi9IRzU0dEZNeWRoUG1SSkVPODR6Yll5ZWZFUkF5clYvVWZFSDRyR0prOTYzYjdqZ3dlWExKaWF0cnVsNkNVcGxjYytxUWpZWnoyZEpHOTBUS0xzR2RMV1UyUlZCOHZkWVZyUFp0TzdTMy0tK2grSCtXbGN4dXUrNXNJdG9iMnMvZz09--2ad27ab84e7e5302561d622329af377920d7544f; tz=Asia%2FShanghai; Hm_lpvt_24f17767262929947cc3631f99bfd274=1710124312; user_return_to_0=%2Fapi%2Fv5%2Fswagger; gitee_user=true; csrf_token=wO6H6Iyz9J8OhxSjV7y%2FWzUnW29okMgJ6Hs10Uau1K%2FT17Z4e62IX9ezJJz9PQNF1d279ZriiPlFgbk4P%2F009w%3D%3D' \
-H 'Sec-Fetch-Dest: empty' \
-H 'Sec-Fetch-Mode: cors' \
-H 'Sec-Fetch-Site: same-origin' \
--data-raw 'utf8=%E2%9C%93&authenticity_token=zKv%2B8najDxCg4D4YMZhi%2FFRylRNk1Wq3uVjuKFmMuDDfks9igb1z0HnUDiebGd7itIh1iZanKkcUomLBIN9YaA%3D%3D&project%5Bimport_url%5D=https%3A%2F%2Fgithub.com%2FNVlabs%2Fcub.git&user_sync_code=prgrmz00&password_sync_code=&project%5Bname%5D=NVlabs--cub&project%5Bnamespace_path%5D=mirrr&project%5Bpath%5D=NVlabs--cub&project%5Bdescription%5D=%E5%AF%BC%E5%85%A5github%E4%BB%93%E5%BA%93NVlabs%2Fcub&project%5Bpublic%5D=1&language=0'

# 确认步骤:
#    3.0. firefox正常 打开页面 https://gitee.com/mirrr/NVlabs--cub.git  ，并删除该仓库
#    3.1  执行 步骤3 中的 curl命令， 则 https://gitee.com/mirrr/NVlabs--cub.git 被正常导入
#    3.2  说明 步骤3 中的 curl命令 确实是 导入给定url接口 


# -H 'Cookie:*' 经过 url解码、分号后加换行 后 如下：
Cookie: sensorsdata2015jssdkcross={"distinct_id":"1895999","first_id":"18e2b2e2deee02-0ed4ffee05327f8-47380724-2073600-18e2b2e2defc0c","props":{"$latest_traffic_source_type":"直接流量","$latest_search_keyword":"未取到值_直接打开","$latest_referrer":""},"identities":"eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMThlMTczNjU2MWMyOGUtMDdhMGQ1ODI0ODU3MTctNDczODA3MjQtMjA3MzYwMC0xOGUxNzM2NTYxZDZjNSIsIiRpZGVudGl0eV9sb2dpbl9pZCI6IjE4OTU5OTkifQ==","history_login_id":{"name":"$identity_login_id","value":"1895999"},"$device_id":"18e1736561c28e-07a0d582485717-47380724-2073600-18e1736561d6c5"};
 sensorsdata2015jssdkchannel={"prop":{"_sa_channel_landing_url":""}};
 user_locale=zh-CN;
 oschina_new_user=false;
 Hm_lvt_24f17767262929947cc3631f99bfd274=1709941077,1709946541,1710038395,1710121431;
 remote_way=ssh;
 visit-gitee--2024-03-06=1;
 yp_riddler_id=75f1f438-d58b-47c2-92a2-e0c4ee6b3674;
 slide_id=10;
 BEC=1f1759df3ccd099821dcf0da6feb0357;
 gitee-session-n=SEFCNjlubWNDNE5sbmVzck1ndmVwUTFyN2g2T1NBNFUrOTF6cU1FY0NqYkJTTEJiMC8yRjZxd1ZGVDROOVhndlFGeTJXd0IyY1dFYnltdGtUYStoQ3VZZjBoNkZ2cXNWWTNGb294NzVmTXZGRGtQMmRoN29LUUl5SFd2SzRIWjFUWEpjQWx0blFTSGpsd3cyWUpnYWt0c3ZiM0tQUGRFY3B6WmdmeXFFYTVUc25zbHdRK1U0NTdEYTJCQVRBb3RCT2V0MHZMdkgxVUwvc2I0cFFJZmIrcy9PMjFXd29RSHRYVUd0eDBzL0JnaWlaU0F4TmMvd0Q1ZDdQSjA0U2RRQVRmb2xvMGJ4VHVhRmYyTkhzSkZPNW1YRnhabTAxcVF0SFV3bVM5azVOVThrMUJUZHdrbHZTc0R0MW92YVlvZG1LTlZ4MDZub3hIWGF2TDI3NkhKYmNKbklLY1o4K0V6Q1B6L3h2eVVhYllEaytRTDQwMVhKVFVNeFcxbVhOdnVTTzZTVnlvcUlPRmlIODZJL3pwZ2Y4OVR0WC8zZWRiUW52N1dzNHFyQUxsWmVKcjBvRHVtVWd3VEk4dFVjTWJ2U3QwNXlZdU1XcXU4eEswZFY3ZlljdS9TQjRRYTYvTHJ1TkxvZWVwZVJIa1lSS0FlTzFVVGdycVRqUFFPeUhlRkl3N1FSTlo1RXRMWTlmWTR3aVhIWXgzQi9IRzU0dEZNeWRoUG1SSkVPODR6Yll5ZWZFUkF5clYvVWZFSDRyR0prOTYzYjdqZ3dlWExKaWF0cnVsNkNVcGxjYytxUWpZWnoyZEpHOTBUS0xzR2RMV1UyUlZCOHZkWVZyUFp0TzdTMy0tK2grSCtXbGN4dXUrNXNJdG9iMnMvZz09--2ad27ab84e7e5302561d622329af377920d7544f;
 tz=Asia/Shanghai;
 Hm_lpvt_24f17767262929947cc3631f99bfd274=1710124312;
 user_return_to_0=/api/v5/swagger;
 gitee_user=true;
 csrf_token=wO6H6Iyz9J8OhxSjV7y/WzUnW29okMgJ6Hs10Uau1K/T17Z4e62IX9ezJJz9PQNF1d279ZriiPlFgbk4P/009w==

# --data-raw 经过 url解码、'&'后加换行 后 如下：
utf8=✓&
authenticity_token=zKv+8najDxCg4D4YMZhi/FRylRNk1Wq3uVjuKFmMuDDfks9igb1z0HnUDiebGd7itIh1iZanKkcUomLBIN9YaA==&
project[import_url]=https://github.com/NVlabs/cub.git&
user_sync_code=prgrmz00&
password_sync_code=&
project[name]=NVlabs--cub&
project[namespace_path]=mirrr&
project[path]=NVlabs--cub&
project[description]=导入github仓库NVlabs/cub&
project[public]=1&
language=0

#4. 接口调用步骤
#术语： 异步导入给定url仓库接口 == 导入给定url接口 == 接口
#术语:  接口的curl例子 == 接口例子,  '<--' 为 覆盖（赋值）操作
#   显然，接口的业务参数 都在 --data-raw 中， 因此 
# 操作步骤为:
#   4.0  gitee页面 正常登录帐号,  以 获取 "-H 'Cookie:*" 、 "-H 'X-CSRF-Token*" 、 "--data-raw .'4.3.2其余字段' "
#   4.1  人工做 步骤2、步骤3 ， 以获得 接口的curl例子
#   4.2  做 url解码('接口例子.--data-raw') 
#   4.3  做 各字段处理( 'url解码(接口例子.--data-raw)' )  ， "各字段处理" 定义 如下: 
#     4.3.1  其中 业务字段 替换为 目标github仓库实际值 ， 业务字段： project[import_url]  、 project[name] 、  project[namespace_path] 、 project[path] 、 project[description] 、 project[public] 、 language ， 
#     4.3.2  其余字段 保持不变，  其余字段： utf8 、 authenticity_token 、 user_sync_code 、password_sync_code
#   4.4  做 :
#            接口例子.--data-raw  <--  url编码( '各字段处理( url解码(接口例子.--data-raw) )' )    
#   4.5  执行 此时的 接口例子 ，即可 在 将 目标github仓库 导入到 gitee中 
