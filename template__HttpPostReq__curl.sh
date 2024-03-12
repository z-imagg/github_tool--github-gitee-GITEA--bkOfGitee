#!/usr/bin/env bash

#【文件作用】 gitee页面的 异步导入给定url仓库接口 请求模板

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
--data-raw "$(cat template__HttpPostReqBdyUrlEncoded.txt)"
