## 使用手册

【本节概要】

以下以pytorch为例子， 演示 ：

- 步1. 将  https://github.com/pytorch/pytorch.git 导入 为 https://gitee.com/imagg/pytorch--pytorch.git 
- 步2. 将  https://github.com/pytorch/pytorch.git 中的子模块们 导入 为 https://gitee.com/imagg/ORG--REPO.git
- 步3. 将  https://github.com/pytorch/pytorch.git 对应的gitee镜像 迁移到 本地 gitea服务 中
- 步4. 将  本地镜像仓库/fridaAnlzAp/gitee/imagg/pytorch--pytorch/下的子模块们 迁移到 本地 gitea服务 中
【详细叙述】
- 步5、 从 "假github"(本地gitea服务) 正常克隆仓库、及其子模块们

**步0 只做一次， 即可供给多次 步1、步2 使用**

#### 步0、 生成gitee导入仓库请求模板(会启动chrome)


```bash -x /fridaAnlzAp/github-gitee-gitea/gitee_api_fetch_ts/script/gen_gitee_import_repo_req_template.sh```

#### 步1、 导入父仓库（github-->gitee）

#####  bash命令提示
```shell
export PATH=/fridaAnlzAp/github-gitee-gitea/gitee_api_fetch_ts/script:$PATH
source /fridaAnlzAp/github-gitee-gitea/gitee_api_fetch_ts/script/bash-complete--import_githubRepo_to_gitee.sh
chmod +x /fridaAnlzAp/github-gitee-gitea/gitee_api_fetch_ts/script/import_githubRepo_to_gitee.sh
```

##### 执行命令
```shell
cd /fridaAnlzAp/gitee/imagg/

import_githubRepo_to_gitee.sh --from_repo https://github.com/pytorch/pytorch.git  --goal_org imagg  --goal_repoPath pytorch--pytorch --goal_repoName pytorch--pytorch  --goal_repoDesc 来源https://github.com/pytorch/pytorch.git

#/fridaAnlzAp/gitee/imagg/pytorch--pytorch/.git/

cd /fridaAnlzAp/gitee/imagg/pytorch--pytorch/
git checkout v1.3.1
```

#### 步2、 导入各子模块（github-->gitee）

#####  bash命令提示
```shell
export PATH=/fridaAnlzAp/github-gitee-gitea/git_submodule_import_cmd_gen/:$PATH
source /fridaAnlzAp/github-gitee-gitea/git_submodule_import_cmd_gen/script/bash-complete--gitSubmoduleImportCmdGen.sh
chmod +x /fridaAnlzAp/github-gitee-gitea/git_submodule_import_cmd_gen/gitSubmoduleImportCmdGen.py
```


##### 执行命令
```shell
bash /fridaAnlzAp/github-gitee-gitea/git_submodule_import_cmd_gen/script/env_prepare.sh
source /fridaAnlzAp/github-gitee-gitea/git_submodule_import_cmd_gen/.venv/bin/activate
gitSubmoduleImportCmdGen.py --parent_repo_dir /fridaAnlzAp/gitee/imagg/pytorch--pytorch  --goal_org imagg  --sleep_seconds 8 --sleep_seconds_delta 9 | bash -x
deactivate
```


torch的[2770e3addd9f05101705f0fef85a163e0034b8a5](https://github.com/pytorch/pytorch/tree/2770e3addd9f05101705f0fef85a163e0034b8a5)  的  [子模块导入日志](http://giteaz:3000/wiki/github-gitee-gitea/src/branch/main/git_submodule_import_cmd_gen/doc/example_submodule_import--2770e3addd9f05101705f0fef85a163e0034b8a5.log.txt)

troch版本[v1.3.1](https://github.com/pytorch/pytorch/commits/refs/tags/v1.3.1/) 【 [ee77ccbb6da4e2efd83673e798acf7081bc03564](https://github.com/pytorch/pytorch/commit/ee77ccbb6da4e2efd83673e798acf7081bc03564) 】
的[子模块导入日志](http://giteaz:3000/wiki/github-gitee-gitea/src/branch/main/git_submodule_import_cmd_gen/doc/example_torch-v1.3.1_submodule_import--v_1.3.1--ee77ccbb6da4e2efd83673e798acf7081bc03564.log.txt)

----


#### 步3和步4、 公共内容

#####  搭建本地gitea服务

[gitea_as_github.md](http://giteaz:3000/wiki/github-gitee-gitea/src/branch/main/localGitea_as_github/gitea_as_github.md)


##### use-local-gitea-as-github

将 搭建好的gitea服务 当作 假"github" 
```shell
echo """
10.0.4.23 github.local
10.0.4.23 github.com
""" | sudo tee -a /etc/hosts
```

#####  bash命令提示
```shell
export PATH=/fridaAnlzAp/github-gitee-gitea/localGitea_as_github/:$PATH
source /fridaAnlzAp/github-gitee-gitea/localGitea_as_github/script/bash-complete--repoMigrateToGitea.sh
chmod +x /fridaAnlzAp/github-gitee-gitea/localGitea_as_github/repoMigrateToGitea.py

source /fridaAnlzAp/github-gitee-gitea/localGitea_as_github/script/bash-complete--submoduleMigrateToGitea.sh
chmod +x /fridaAnlzAp/github-gitee-gitea/localGitea_as_github/submoduleMigrateToGitea.py
```


#### 步3、 迁移父仓库（gitee-->本地gitea）

##### 执行命令
```shell
bash /fridaAnlzAp/github-gitee-gitea/localGitea_as_github/script/env_prepare.sh
source /fridaAnlzAp/github-gitee-gitea/localGitea_as_github/.venv/bin/activate
repoMigrateToGitea.py --from_repo_url https://github.com/pytorch/pytorch.git  --mirror_base_ur https://gitee.com  --mirror_org_name imagg
```

#### 步4、迁移各子模块（gitee-->本地gitea）

submoduleMigrateToGitea.py有丢失子模块, 改用git命令列出子模块后再迁移仓库

```shell
alias AliasXargsGitConfigGetUrlAwkPrint2Xargs_RepoMigrateToGitea_py_gitee_imagg='xargs -I@ git --no-pager  config --file @  --get-regexp url  | awk "{ print \$2 }" | xargs -I% repoMigrateToGitea.py --from_repo_url % --mirror_base_ur https://gitee.com  --mirror_org_name imagg'
```

```shell
#此时只迁移直接子模块，不迁移子子模块。因为子模块内容没更新，所以看不到子模块的子模块
echo "/fridaAnlzAp/gitee/imagg/pytorch--pytorch/.gitmodules"  | AliasXargsGitConfigGetUrlAwkPrint2Xargs_RepoMigrateToGitea_py_gitee_imagg
#即使写成下面的find，也只找到直接目录下的一个.gitmodules文件，所以此时下面的find和上面的echo效果一致
# find /fridaAnlzAp/gitee/imagg/pytorch--pytorch/ -name .gitmodules -type f  | AliasXargsGitConfigGetUrlAwkPrint2Xargs_RepoMigrateToGitea_py_gitee_imagg

#注意时候， 现在没有  "假github" 供给你更新子模块，  "假github"(即本地gitea服务) 在 步5 才有。
```

#### ~~步4、 迁移各子模块（gitee-->本地gitea）~~(submoduleMigrateToGitea.py有丢失子模块)


##### 执行命令
```shell
bash /fridaAnlzAp/github-gitee-gitea/localGitea_as_github/script/env_prepare.sh
source /fridaAnlzAp/github-gitee-gitea/localGitea_as_github/.venv/bin/activate
submoduleMigrateToGitea.py --from_parent_repo_dir /fridaAnlzAp/gitee/imagg/pytorch--pytorch/  --mirror_base_ur https://gitee.com  --mirror_org_name imagg
```

没捕捉到从无到有导入子仓库们的日志，这是重新执行的日志了 , http://giteaz:3000/wiki/github-gitee-gitea/src/branch/main/localGitea_as_github/doc/example_out_ReExec_submoduleMigrateToGitea__pytorch_v1.3.1.log.txt


#### 步5、 从 "假github"(本地gitea服务) 正常克隆仓库、及其子模块们

由于 , [use-local-gitea-as-github](http://giteaz:3000/wiki/github-gitee-gitea#use-local-gitea-as-github)

因此 可以 正常从 "假github" 克隆 pytorch仓库了,

#####  clone
```shell
cd /fridaAnlzAp/
git clone https://github.com/pytorch/pytorch.git
#/fridaAnlzAp/pytorch/.git/config
```
pytorch克隆日志, [pytorch_clone-out.log.txt](http://giteaz:3000/wiki/github-gitee-gitea/src/branch/main/localGitea_as_github/doc/pytorch_clone-out.log.txt)


##### checkout v1.3.1
```shell
cd /fridaAnlzAp/pytorch/
git checkout v1.3.1
```

##### 更新直接子模块 
```shell
#更新 /fridaAnlzAp/pytorch 中的 子模块们， 也 将一样是 正常从 "假github" 克隆到的
#当让 如果有 lazygit 去更新子模块也一样的
git submodule update --init   --progress 
#不要加选项 --recursive 、 --depth N ，（N是1、2、3...）， 理由是 一个源码仓库torch-v1.3.1要正常编译 是会依赖子模块，但通常其子模块对子子模块？？？暂时不考虑 ，等编译时遇到问题再说。
```
pytorch更新子模块的输出日志, [pytorch_submodule_update_init_progress-out.log.txt](http://giteaz:3000/wiki/github-gitee-gitea/src/branch/main/localGitea_as_github/doc/pytorch_submodule_update_init_progress-out.log.txt)

##### 迁移子子模块
```shell
#下面的find会找到多个.gitmodules文件
find /fridaAnlzAp/pytorch/ -name .gitmodules -type f  | AliasXargsGitConfigGetUrlAwkPrint2Xargs_RepoMigrateToGitea_py_gitee_imagg
```

## 网页(可重执行)请求协议分析方案


**可重执行 即 同一个请求可原样多次执行 即 无签名字段**


### 半通用、半自动 方案（有吸引力）


基于nodejs实现的，  http://giteaz:3000/msic/node-typescript-boilerplate.git

大致步骤：

以chrome-remote-interface驱动chrome浏览器，

1. 人工登录gitee账户、

2. 打开目标网页 用js操作dom以填充固定的标记参数 点击按钮  以 获得 含有标记字段值的请求例子 （具体是 gitee导入URL仓库页面 各字段填充固定标记值  ）、 

3. 替换 请求例子 中的标记字段值 为 新参数值、 

4. 执行新请求 



###  ~~朴素方案（无吸引力）~~


基于python实现的，  http://giteaz:3000/wiki/github-gitee-gitea/src/commit/8e4c365ae83249ef6928a5c3da306f97f47c2d1d/github_to_gitee


大致步骤：

1. 人工 使用 浏览器开发者工具 拿到 关心的请求的curl例子 (即 例子请求) （具体是 gitee导入URL仓库页面   ）

2. 解开例子请求体、

3. 按字段名设置填充新参数值、 

4. 组装为新请求体 （步骤4是步骤2的逆过程）

5. 执行新请求
