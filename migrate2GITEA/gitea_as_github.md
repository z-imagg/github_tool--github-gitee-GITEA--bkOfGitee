【文件作用】 docker内部署gitea，向其内导入gitee.com/mirrr/org--repo.git, 即将gitea当作github.com

----
宿主机ip地址为10.0.4.23
```shell
ip address
#wlo1 : inet 10.0.4.23/24 brd 10.0.4.255 scope global noprefixroute wlo1
```
----
```shell

#docker创建网络（交换机？）
docker network create --driver bridge --subnet 172.23.0.0/16  --gateway 172.23.0.1 dckBrgNet
docker network ls
# NETWORK ID     NAME        DRIVER    SCOPE
# 5c0ff505873e   bridge      bridge    local
# 254b00dcde44   dckBrgNet   bridge    local
# 4f0e3ec7ae07   host        host      local
# 191c4ad8b87f   none        null      local

#docker network rm dckBrgNet

mkdir -p /app/github_local_home/
#docker ps -a
# docker stop u22.04_gitea
# docker rm u22.04_gitea
#创建docker实例，指定该网络中ip
docker run --interactive  --tty  --detach \
--network dckBrgNet \
--ip 172.23.0.9 \
-p 10.0.4.23:443:3000  \
-v /app/github_local_home/:/app/github_local_home/ \
--name  u22.04_gitea   \
ubuntu:22.04

docker exec  --interactive --tty  u22.04_gitea  bash
```
----
宿主机 添加本地域名
```shell
echo """
10.0.4.23 github.local
10.0.4.23 github.com
""" | sudo tee -a /etc/hosts
```

等后面正常启动gitea服务后， 

- 浏览器上 访问 此gitea ， 地址 是  https://github.local:443  , 443可省略  
 
- 浏览器 以地址 https://github.com:443  并不能访问到 此gitea   , 443可省略  

（估计 原因是因为 浏览器 对 知名域名 比如 github 做了特殊处理）

- 命令行 能正常 以 github.com 克隆 此gitea中的仓库 ```git clone https://github.com/NVlabs/cub.git```

----
docker实例  添加本地域名
```shell
echo """
172.23.0.9 github.local
172.23.0.9 github.com
""" | tee -a /etc/hosts
```
----
**以下在docer实例内执行**

----
```apt update```

docker实例内查看到的ip地址确实是上面创建docker实例时指定的
```shell
apt install net-tools
ifconfig
# eth0: inet 172.23.0.9  netmask 255.255.255.0  broadcast 172.23.0.255
```
----
```apt install -y git```

----
https://github.com/go-gitea/gitea/releases/tag/v1.21.7
```shell
cd /app/github_local_home/
wget https://github.com/go-gitea/gitea/releases/download/v1.21.7/gitea-1.21.7-linux-amd64
```
----
```shell
deluser --force --remove-home g
adduser g

su - g
cd /app/github_local_home/
nohup ./gitea-1.21.7-linux-amd64 web &
```
----
宿主机 浏览器访问 http://github.local:443  ,   此时 是 gitea第一次启动 还没有启用https， 因此 443 --> 3000 实际上 是 http协议
- 数据库: SqLite
- 服务器域名: github.local
- 基础URL: https://github.local/
- 服务器和第三方设置中, 勾选 "启用本地模式"、 勾选"禁止Gravatar头像" 、 不勾选"Federated头像" 

（如果不禁止*头像，则正常访问gitea的web页面会一直试图获取到拿不到的西方服务器上的头像 表现为浏览器一直转圈圈 很烦）
- 其余默认
点击"立即安装", 后 点击"注册" 手动注册一用户（用户名:root 、 密码:11111111 、 邮箱:root@x.com）


---- 

gitea 配置https

参照修改 app.ini,  https://docs.gitea.com/zh-cn/next/administration/https-setup
修改内容, ```cd /app/github_local_home/custom/conf/;  diff -u  app.ini.origin app.ini```
```diff
--- /app/github_local_home/custom/conf/app.ini.origin	2024-03-11 23:19:54.737726300 +0800
+++ /app/github_local_home/custom/conf/app.ini	2024-03-11 23:21:39.073144800 +0800
@@ -18,16 +18,19 @@
 ROOT = /app/github_local_home/data/gitea-repositories
 
 [server]
+PROTOCOL  = https
 SSH_DOMAIN = github.local
 DOMAIN = github.local
 HTTP_PORT = 3000
-ROOT_URL = http://github.local/
+ROOT_URL = https://github.local/
 APP_DATA_PATH = /app/github_local_home/data
 DISABLE_SSH = false
 SSH_PORT = 22
 LFS_START_SERVER = true
 LFS_JWT_SECRET = RKpIy9aRq-HpUq9kRLptZiJR9jOTs0rOp9ZJ86mt1YE
 OFFLINE_MODE = true
+CERT_FILE = cert.pem
+KEY_FILE  = key.pem
 
 [lfs]
 PATH = /app/github_local_home/data/lfs
```


```shell
su - g
cd /app/github_local_home/custom/
/app/github_local_home/gitea-1.21.7-linux-amd64 cert --host github.local
# 2024/03/11 15:23:49 Written cert.pem
# 2024/03/11 15:23:49 Written key.pem
```

重启 gitea

- docker实例内 终端执行 , 正常， ```curl -k  https://github.local:3000```

- 宿主机 浏览器访问 ， 正常， https://github.local:443  , 443可省略

- 宿主机 终端克隆 ， 正常， ```git clone https://github.com:443```   , 443可省略



- 这里没有配置http转发到https, 没必要 ，简单能用即可，因此按本文  http://github.local  是不能访问的

----

允许gitea从任意域名导入仓库, https://docs.gitea.com/next/administration/config-cheat-sheet#migrations-migrations
```shell
echo """
[migrations]
ALLOW_LOCALNETWORKS = true
ALLOWED_DOMAINS = gitee.com,*
""" >> /app/github_local_home/custom/conf/app.ini
```
----

重启gitea

---
访问 https://github.local  , 人工导入仓库正常 http://gitee.com/mirrr/NVlabs--cub.git

----
gitea 文档说 其有swagger页面， https://docs.gitea.com/next/development/api-usage#api-guide

gitea swagger 中的 导入仓库接口文档， https://github.local/api/swagger#/repository/repoMigrate

----

设置--->应用， 创建令牌(token) 启用所有权限， token形如 b1d490eaf6b88a6c37bd482d8e05e3a0061f066c ,  https://github.local/user/settings/applications

swagger页面 顶部 左边， 点击 按钮"Authorize"  在 "Token (apiKey)" 处 填入 token ， 该token会携带在swagger页面的每个请求上 方便开发调试， https://github.local/api/swagger#/

----

创建组织,  https://github.local/api/swagger#/organization/orgCreate

```shell
curl -k -X 'POST' \
  'https://github.local/api/v1/orgs?token=b1d490eaf6b88a6c37bd482d8e05e3a0061f066c' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "username": "NVlabs",
  "repo_admin_change_team_access": true,
  "visibility": "public"
}'
```

```json
{
  "id": 3,
  "name": "NVlabs",
  "full_name": "",
  "email": "",
  "avatar_url": "https://github.local/avatars/5d9964cf11af89a3af320fb218803cef",
  "description": "",
  "website": "",
  "location": "",
  "visibility": "public",
  "repo_admin_change_team_access": true,
  "username": "NVlabs"
}
```
----

以 "迁移外部仓库（从Git迁移）" 导入 gitee仓库 到此gitea， https://github.local/api/swagger#/repository/repoMigrate

这是一个同步接口， 导入仓库完成 才会返回

调用完 此接口， 在 宿主机 可以 正常克隆到 "github仓库", 注意是http 不是https, ```git clone https://github.com/NVlabs/cub.git``` ,  https://github.com/NVlabs/cub.git

```shell
curl -k -X 'POST' \
  'https://github.local/api/v1/repos/migrate?token=b1d490eaf6b88a6c37bd482d8e05e3a0061f066c' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "clone_addr": "https://gitee.com/mirrr/NVlabs--cub.git",
  "repo_name": "cub",
  "repo_owner": "NVlabs"
}'
```


```json
{"id":1,
"owner":{"id":2,"login":"NVlabs","login_name":"","full_name":"","email":"","avatar_url":"https://github.local/avatars/5d9964cf11af89a3af320fb218803cef",
"language":"","is_admin":false,"last_login":"0001-01-01T00:00:00Z","created":"2024-03-11T16:17:44Z","restricted":false,"active":false,"prohibit_login":false,"location":"","website":"","description":"","visibility":"public","followers_count":0,"following_count":0,"starred_repos_count":0,"username":"NVlabs"},
"name":"cub","full_name":"NVlabs/cub","description":"","empty":false,"private":false,"fork":false,"template":false,"parent":null,"mirror":false,"size":25,"language":"","languages_url":"https://github.local/api/v1/repos/NVlabs/cub/languages",
"html_url":"https://github.local/NVlabs/cub","url":"https://github.local/api/v1/repos/NVlabs/cub","link":"","ssh_url":"g@github.local:NVlabs/cub.git",
"clone_url":"https://github.local/NVlabs/cub.git","original_url":"https://gitee.com/mirrr/NVlabs--cub.git","website":"","stars_count":0,"forks_count":0,"watchers_count":1,"open_issues_count":0,"open_pr_counter":0,"release_counter":0,"default_branch":"main","archived":false,"created_at":"2024-03-11T16:18:23Z","updated_at":"2024-03-11T16:18:28Z","archived_at":"1970-01-01T00:00:00Z",
"permissions":{"admin":true,"push":true,"pull":true},
"has_issues":true,
"internal_tracker":{"enable_time_tracker":true,"allow_only_contributors_to_track_time":true,"enable_issue_dependencies":true},
"has_wiki":true,"has_pull_requests":true,"has_projects":true,"has_releases":true,"has_packages":true,"has_actions":false,"ignore_whitespace_conflicts":false,
"allow_merge_commits":true,"allow_rebase":true,"allow_rebase_explicit":true,"allow_squash_merge":true,"allow_rebase_update":true,
"default_delete_branch_after_merge":false,"default_merge_style":"merge","default_allow_maintainer_edit":false,"avatar_url":"","internal":false,"mirror_interval":"","mirror_updated":"0001-01-01T00:00:00Z","repo_transfer":null}

```


----

部分浏览器 正常访问 https://github.com 


- firefox 不允许 访问 https://github.com ,  报错 错误代码：MOZILLA_PKIX_ERROR_SELF_SIGNED_CERT

- chrome 不允许 访问 https://github.com , 报错 

- epiphany-browser 访问 https://github.com ， 提示 "连接不安全",  选择 接受 后 ，正常访问 


- 浏览器(包括firefox) 访问 https://github.local 是正常的 


----

终端git命令克隆github.com仓库 正常

```shell
git config --global http.sslVerify false

git config --global --unset http.https://github.com.proxy
git config --global --unset https.https://github.com.proxy

git clone https://github.local/NVlabs/cub.git #正常

git clone https://github.com/NVlabs/cub.git  #正常， 且 gitea进程有日志打印 说明访问的是 gitea伪装的本地假github.com 而非真实github.com

```