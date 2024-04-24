
[开发用的详细文档==readme-dev.md](http://giteaz:3000/wiki/github-gitee-GITEA/src/branch/main/readme-dev.md)

[客户方简易使用文档==readme.md](http://giteaz:3000/wiki/github-gitee-GITEA/src/branch/main/readme.md)



**本文是 客户方简易使用文档**

### 环境安装、依赖安装(只做一次)
```shell
bash /fridaAnlzAp/github-gitee-GITEA/script/env_prepare.sh 

cd /fridaAnlzAp/github-gitee-GITEA/gitee_api_fetch_ts/ && npm install

```

### 前置准备(只做一次)

####  1. 生成gitee导入仓库请求模板(会启动chrome) 

##### 1.1 准备gitee.com帐号

复制[gitee_account.json.template](http://giteaz:3000/misc/node-typescript-boilerplate/src/branch/main/gitee_account.json.template)为同目录下文件gitee_account.json, 并按照模板中字段提示填充字段值

##### 1.2 生成请求模板
```bash -x /fridaAnlzAp/github-gitee-GITEA/gitee_api_fetch_ts/script/gen_gitee_import_repo_req_template.sh```



####  2. 搭建本地gitea服务

[gitea_as_github.md](http://giteaz:3000/wiki/github-gitee-GITEA/src/branch/main/migrate2GITEA/gitea_as_github.md)


##### use-local-gitea-as-github

将 搭建好的gitea服务 当作 假"github" 
```shell
echo """
10.0.4.23 github.local
10.0.4.23 github.com
""" | sudo tee -a /etc/hosts
```




###  pytorch v0.3.0


#### 1、 递归gitee导入接口（github-->gitee）

TODO 


#### 2、迁移迁移(gitee-->本地GITEA)


```shell
RepoRecurseMigrate.py --from_repo_url https://github.com/pytorch/pytorch.git --from_commit_id af3964a8725236c78ce969b827fdeee1c5c54110 --mirror_base_ur https://gitee.com --mirror_org_name imagg --sleep_seconds 2 
```

#### 3、 编译 

http://giteaz:3000/wiki/github-gitee-GITEA/src/branch/main/torch-v0.3.0-build.md


###  pytorch v1.0.0

#### 1、 递归gitee导入接口（github-->gitee）


```shell
RepoRecurseImport.py  --from_repo_url https://github.com/pytorch/pytorch.git --from_commit_id db5d3131d16f57abd4f13d3f4b885d5f67bf6644 --goal_org imagg --sleep_seconds 2 
    

```

http://giteaz:3000/wiki/github-gitee-GITEA/src/branch/main/import2gitee/doc/import_torch-v1.0.0-db5d3131d16f57abd4f13d3f4b885d5f67bf6644.log.txt

----

#### 2、迁移迁移(gitee-->本地GITEA)


```shell
RepoRecurseMigrate.py --from_repo_url https://github.com/pytorch/pytorch.git --from_commit_id db5d3131d16f57abd4f13d3f4b885d5f67bf6644 --mirror_base_ur https://gitee.com --mirror_org_name imagg --sleep_seconds 2 
```

#### 3、 编译 

http://giteaz:3000/wiki/github-gitee-GITEA/src/branch/main/torch-v1.0.0-build.md

#### 4、 c++例子

https://gitee.com/frida_analyze_app_src/torch-cpp/blob/master/v1.0.0/readme.md



###  pytorch v1.3.1


#### 1、 递归gitee导入接口（github-->gitee）

TODO

#### 2、迁移迁移(gitee-->本地GITEA)

TODO

#### 3、  编译 

http://giteaz:3000/wiki/github-gitee-GITEA/src/branch/main/torch-v1.3.1-build.md


