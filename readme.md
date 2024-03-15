## 使用手册

#### 1. 导入父仓库

```shell
cd /fridaAnlzAp/gitee/orgk/

import_githubRepo_to_gitee.sh --from_repo https://github.com/pytorch/pytorch.git  --goal_org imagg  --goal_repoPath pytorch--pytorch --goal_repoName pytorch--pytorch  --goal_repoDesc 来源https://github.com/pytorch/pytorch.git

#/fridaAnlzAp/gitee/imagg/pytorch--pytorch/.git/

cd /fridaAnlzAp/gitee/imagg/pytorch--pytorch/
git checkout v1.3.1
```

#### 2. 导入各子模块

```shell
#bash命令提示
export PATH=/fridaAnlzAp/github-gitee-gitea/git_submodule_import_cmd_gen/:$PATH
source /fridaAnlzAp/github-gitee-gitea/git_submodule_import_cmd_gen/script/bash-complete--gitSubmoduleImportCmdGen.sh
chmod +x /fridaAnlzAp/github-gitee-gitea/git_submodule_import_cmd_gen/gitSubmoduleImportCmdGen.py
```


```shell
bash /fridaAnlzAp/github-gitee-gitea/git_submodule_import_cmd_gen/script/env_prepare.sh
source /fridaAnlzAp/github-gitee-gitea/git_submodule_import_cmd_gen/.venv/bin/activate
gitSubmoduleImportCmdGen.py --parent_repo_dir /fridaAnlzAp/gitee/imagg/pytorch--pytorch  --goal_org imagg  --sleep_seconds 8 --sleep_seconds_delta 9 | bash -x
deactivate
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