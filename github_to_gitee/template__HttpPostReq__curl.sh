#!/usr/bin/env bash

#【文件作用】 gitee页面的 异步导入给定url仓库接口 请求模板， 包含gitee接口调用凭据
#【文件来源】
#  人工做 "gitee从URL导入： https://gitee.com/projects/import/url" 过程中 , 浏览器开发者工具捕捉到的 的一次地址 https://gitee.com/mirrr/projects 为的请求, 即为以下curl内容

curl 'https://gitee.com/tmpOrg/projects' --connect-timeout 15 --max-time 30   --compressed -X POST \
-H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0' \
-H 'Accept: text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01' \
-H 'Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2' \
-H 'Accept-Encoding: gzip, deflate, br' \
-H 'Referer: https://gitee.com/projects/import/url' \
-H 'X-CSRF-Token: WPPHocVtxygNDVZlB1js+2/PB4cLkfR7x+scErL+fjvoyQfiqeCOsymzaWbbX5k8cLGWN1kafSyoQE8nHGfV7A==' \
-H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' \
-H 'X-Requested-With: XMLHttpRequest' \
-H 'Origin: https://gitee.com' \
-H 'Connection: keep-alive' \
-H 'Cookie: sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221895999%22%2C%22first_id%22%3A%2218e303df01e100-0bb11c4dd181708-47380724-2073600-18e303df01f1b07%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMThlMTczNjU2MWMyOGUtMDdhMGQ1ODI0ODU3MTctNDczODA3MjQtMjA3MzYwMC0xOGUxNzM2NTYxZDZjNSIsIiRpZGVudGl0eV9sb2dpbl9pZCI6IjE4OTU5OTkifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%221895999%22%7D%2C%22%24device_id%22%3A%2218e1736561c28e-07a0d582485717-47380724-2073600-18e1736561d6c5%22%7D; sensorsdata2015jssdkchannel=%7B%22prop%22%3A%7B%22_sa_channel_landing_url%22%3A%22%22%7D%7D; user_locale=zh-CN; oschina_new_user=false; Hm_lvt_24f17767262929947cc3631f99bfd274=1709946541,1710038395,1710121431,1710206345; remote_way=http; visit-gitee--2024-03-06=1; yp_riddler_id=75f1f438-d58b-47c2-92a2-e0c4ee6b3674; slide_id=10; BEC=1f1759df3ccd099821dcf0da6feb0357; csrf_token=kfjjOnFFzGIGrun%2BmsMTDKHo6GbQAyoBkMGnZuoQzWwhwiN5HciF%2BSIQ1v1GxGbLvpZ51oKIo1b%2FavRTRIlmuw%3D%3D; gitee-session-n=ZERCemVNcDQvbHFjWWFYc2RXZWhxQzNHUW5Cajg3Ulc5ZlhuR0dDc2FxcUN2WGkyM1hhK1NYcUQyQWdzQTFaSDNyRVVQNHA0dys0aDZKNy91QjJvRmhVY1RYWGN6WXdnRzFOdW96bzJCdEtBQ3p1YStlbEJmaVl2ZmJsZGdIRlJPc2ViZFc0R2tzWCtxRFI4aVh3c3A5R3JhbHhSczYvZC9JQU12c253VmllRytYK2ZxNENFSUlGL0N2cDVFdFZvYTRjM09yc096T0hGY3Q0T3V6a3BVMVd6VU1rdDJjcDc4bmJKUGtSaEJkdm1qMkpldWZiOG5RaUNkRUhnb1NxZWM1cmVWaEIyZ1F2YTM3dGJOS0RBTGNlbVlGcWJqdm1jQlJmRzl1MlM1UnE4cDhOZjZ3encxOXJQVXFiZXZYTnNGdHlRVjlyeGlKODNHbVBEQ0NtVE5ORnFKWTM0YWJzL0RjM2FUekNDL2ZKNHoyUzBHNCt1RjN1UVRvd1A1cUZjVEluVy85WHdTMFordkg5QUZ6TmQ3elh2UWJtYm0wRkpGeFQ1cFp0dUVuamZ5djMvZ29zU0w5eVdJY3JYMGZrTExpckVDNnErYVgydVFIUndLcURhSXlrS083dktHdFNoaDN2WXRqZ1hwWTVBaExPSy9WNzB2cGx4ekwyYmpVYXFDdWc4NUZWOCtzVGQ4bm5uSkFmcnl4bGJtd2k4YmRKWHZRNFA1ZkhaNUxoSjR2eWdrcHNPUEpnY3VDaDAxZDlneWkzV2FLSmRpT1h0TGV6ZVJQNWJ4NHVjbmYxbVlDY21hUllCbGhYU0dDM0lSRm9SeHdQdklsOVkwVHlJVFd2Sy0teUtZS3hjbXFkR0E5RVM2dG4zTEx4dz09--322fdaefd141e53a03ec2526ec392ffa9a0cd740; Hm_lpvt_24f17767262929947cc3631f99bfd274=1710212745; user_return_to_0=%2F; tz=Asia%2FShanghai; gitee_user=true' \
-H 'Sec-Fetch-Dest: empty' \
-H 'Sec-Fetch-Mode: cors' \
-H 'Sec-Fetch-Site: same-origin' \
--data-raw "$(cat template__HttpPostReqBdyUrlEncoded.txt)"
