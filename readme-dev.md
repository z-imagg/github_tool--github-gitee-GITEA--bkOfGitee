[开发用的详细文档==readme-dev.md](http://giteaz:3000/wiki/github-gitee-GITEA/src/branch/main/readme-dev.md)

[客户方简易使用文档==readme.md](http://giteaz:3000/wiki/github-gitee-GITEA/src/branch/main/readme.md)


**本文是 开发用的详细文档**

## 使用手册

**0生成导入请求模板、1导入、2迁移、3克隆、4业务**

【本节概要】

以下以pytorch为例子， 演示 ：

- 步1. 【正常 递归gitee导入接口】从一github仓库pytorch的url、其中某commitId为起点  递归地做：调用gitee导入接口、循环等且克隆仓库、递归其子模块列表
- 步2. 【正常 递归本地GITEA迁移接口】从一github仓库pytorch的url、其中某commitId为起点  递归地做： 调用本地GITEA服务的迁移接口、循环等且克隆仓库、递归其子模块列表
【详细叙述】
- 步3、 从 "假github"(本地gitea服务) 正常克隆仓库、及其子模块们
- 步4、 针对该github仓库的正常业务（这里是编译pytorch源码）

**步0 只做一次， 即可供给多次 步1 使用**

#### 步0、 生成gitee导入仓库请求模板(会启动chrome)


```bash -x /app/github-gitee-GITEA/gitee_api_fetch_ts/script/gen_gitee_import_repo_req_template.sh```

#### 步1、 递归gitee导入接口（github-->gitee）

#####  bash命令提示
```shell
source /app/github-gitee-GITEA/script/cmd_setup.sh
#正常可用：RepoRecurseImport.py --help 及其 bash自动完成
#正常可用：RepoRecurseMigrate.py --help 及其 bash自动完成
```

http://giteaz:3000/wiki/github-gitee-GITEA/src/branch/main/script/cmd_setup.sh

##### 执行命令



######  pytorch main

```shell
RepoRecurseImport.py  --from_repo_url https://github.com/pytorch/pytorch.git --from_commit_id ee77ccbb6da4e2efd83673e798acf7081bc03564 --goal_org imagg --sleep_seconds 2 
    
```


######  pytorch v0.3.0

TODO




######  pytorch v1.0.0

```shell
RepoRecurseImport.py  --from_repo_url https://github.com/pytorch/pytorch.git --from_commit_id db5d3131d16f57abd4f13d3f4b885d5f67bf6644 --goal_org imagg --sleep_seconds 2 
    

```

http://giteaz:3000/wiki/github-gitee-GITEA/src/branch/main/import2gitee/doc/import_torch-v1.0.0-db5d3131d16f57abd4f13d3f4b885d5f67bf6644.log.txt

----


#### 步2、迁移迁移(gitee-->本地GITEA)

#####  搭建本地gitea服务

[gitea_as_github.md](http://giteaz:3000/wiki/github-gitee-GITEA/src/branch/main/migrate2GITEA/gitea_as_github.md)


##### use-local-gitea-as-github

将 搭建好的gitea服务 当作 假"github" 
```shell
echo """
10.0.4.23 github.local
10.0.4.23 github.com
""" | sudo tee -a /etc/hosts
```


##### 执行命令

######  pytorch main

```shell
RepoRecurseMigrate.py --from_repo_url https://github.com/pytorch/pytorch.git --from_commit_id ee77ccbb6da4e2efd83673e798acf7081bc03564 --mirror_base_ur https://gitee.com --mirror_org_name imagg --sleep_seconds 2 
```

######  pytorch v0.3.0

```shell
RepoRecurseMigrate.py --from_repo_url https://github.com/pytorch/pytorch.git --from_commit_id af3964a8725236c78ce969b827fdeee1c5c54110 --mirror_base_ur https://gitee.com --mirror_org_name imagg --sleep_seconds 2 
```

https://gitee.com/imagg/pytorch--pytorch/tree/v0.3.0

https://gitee.com/imagg/pytorch--pytorch/commit/af3964a8725236c78ce969b827fdeee1c5c54110


######  pytorch v1.0.0

```shell
RepoRecurseMigrate.py --from_repo_url https://github.com/pytorch/pytorch.git --from_commit_id db5d3131d16f57abd4f13d3f4b885d5f67bf6644 --mirror_base_ur https://gitee.com --mirror_org_name imagg --sleep_seconds 2 
```

#### 步3、 从 "假github"(本地gitea服务) 正常克隆仓库、及其子模块们

由于 , [use-local-gitea-as-github](http://giteaz:3000/wiki/github-gitee-GITEA#use-local-gitea-as-github)

因此 可以 正常从 "假github" 克隆 pytorch仓库了,

#####  clone
```shell
cd /app/
git clone https://github.com/pytorch/pytorch.git
#/app/pytorch/.git/config
```
pytorch克隆日志, [pytorch_clone-out.log.txt](http://giteaz:3000/wiki/github-gitee-GITEA/src/branch/main/migrate2GITEA/doc/pytorch_clone-out.log.txt)


##### checkout v1.3.1
```shell
cd /app/pytorch/
git checkout v1.3.1
```

##### 更新直接子模块 
```shell
#更新 /app/pytorch 中的 子模块们， 也 将一样是 正常从 "假github" 克隆到的
#当让 如果有 lazygit 去更新子模块也一样的
git submodule update --init   --progress 
```
pytorch更新子模块的输出日志, [pytorch_submodule_update_init_progress-out.log.txt](http://giteaz:3000/wiki/github-gitee-GITEA/src/branch/main/migrate2GITEA/doc/pytorch_submodule_update_init_progress-out.log.txt)



#### 步4、 针对该github仓库的正常业务（编译pytorch-v1.3.1）

http://giteaz:3000/wiki/github-gitee-GITEA/src/branch/main/torch-v1.3.1-build.md

#### 步5、 针对该github仓库的正常业务（编译pytorch-v0.3.0）

http://giteaz:3000/wiki/github-gitee-GITEA/src/branch/main/torch-v0.3.0-build.md

----

## 网页(可重执行)请求协议分析方案

 http://giteaz:3000/wiki/github-gitee-GITEA/src/branch/main/markupReq.md