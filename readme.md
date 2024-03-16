## 使用手册

【本节概要】

以下以pytorch为例子， 演示 ：

- 步1. 【正常 递归gitee导入接口】从一github仓库pytorch的url、其中某commitId为起点  递归地做：调用gitee导入接口、循环等且克隆仓库、递归其子模块列表
- 步3. 将  https://github.com/pytorch/pytorch.git 对应的gitee镜像 迁移到 本地 gitea服务 中
- 步4. 将  本地镜像仓库/fridaAnlzAp/gitee/imagg/pytorch--pytorch/下的子模块们 迁移到 本地 gitea服务 中
【详细叙述】
- 步5、 从 "假github"(本地gitea服务) 正常克隆仓库、及其子模块们

**步0 只做一次， 即可供给多次 步1、步2 使用**

#### 步0、 生成gitee导入仓库请求模板(会启动chrome)


```bash -x /fridaAnlzAp/github-gitee-gitea/gitee_api_fetch_ts/script/gen_gitee_import_repo_req_template.sh```

#### 步1、 递归gitee导入接口（github-->gitee）

#####  bash命令提示
```shell
ImportHome=/fridaAnlzAp/github-gitee-gitea/git_submodule_import_cmd_gen
MigrateHome=/fridaAnlzAp/github-gitee-gitea/localGitea_as_github
export PATH=$ImportHome/:$MigrateHome:$PATH
source $ImportHome/script/bash-complete--gitSubmoduleImportCmdGen.sh
source $MigrateHomescript/bash-complete--repoMigrateToGitea.sh
source $MigrateHome/script/bash-complete--submoduleMigrateToGitea.sh
chmod +x $ImportHome/gitSubmoduleImportCmdGen.py
chmod +x $MigrateHome/repoMigrateToGitea.py
chmod +x $MigrateHome/submoduleMigrateToGitea.py

bash /fridaAnlzAp/github-gitee-gitea/script/env_prepare.sh
source /fridaAnlzAp/github-gitee-gitea/.venv/bin/activate
```


##### 执行命令
```shell
cd /fridaAnlzAp/github-gitee-gitea/

./git_submodule_import_cmd_gen/RepoRecurseImport.py  --from_repo_url https://github.com/pytorch/pytorch.git --from_commit_id ee77ccbb6da4e2efd83673e798acf7081bc03564 --goal_org ruut --sleep_seconds 2 
    
```


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


#### 步3、 迁移父仓库（gitee-->本地gitea）

##### 执行命令
```shell
repoMigrateToGitea.py --from_repo_url https://github.com/pytorch/pytorch.git  --mirror_base_ur https://gitee.com  --mirror_org_name imagg
```

#### 步4、迁移各子模块（gitee-->本地gitea）

submoduleMigrateToGitea.py有丢失子模块, 改用git命令列出子模块后再迁移仓库

```shell
find /fridaAnlzAp/pytorch  -name .gitmodules -type f | xargs -I@ git --no-pager  config --file @  --get-regexp url  | awk "{ print \$2 }"  |wc -l
#     45      
#子模块个数，可能还有没更新到的子模块
```

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
submoduleMigrateToGitea.py --from_parent_repo_dir /fridaAnlzAp/gitee/imagg/pytorch--pytorch/  --mirror_base_ur https://gitee.com  --mirror_org_name imagg
```

没捕捉到从无到有导入子仓库们的日志，这是重新执行的日志了 , http://giteaz:3000/wiki/github-gitee-gitea/src/branch/main/localGitea_as_github/doc/example_out_ReExec_submoduleMigrateToGitea__pytorch_v1.3.1.log.txt


----

##### 确定要完整递归整个torch仓库的任意子模块

```shell
find /fridaAnlzAp/pytorch -name .gitmodules
# /fridaAnlzAp/pytorch/.gitmodules
# /fridaAnlzAp/pytorch/third_party/fbgemm/.gitmodules
# /fridaAnlzAp/pytorch/third_party/gloo/.gitmodules
# /fridaAnlzAp/pytorch/third_party/ideep/.gitmodules
# /fridaAnlzAp/pytorch/third_party/onnx/.gitmodules
# /fridaAnlzAp/pytorch/third_party/onnx/third_party/pybind11/.gitmodules
# /fridaAnlzAp/pytorch/third_party/onnx-tensorrt/.gitmodules
# /fridaAnlzAp/pytorch/third_party/onnx-tensorrt/third_party/onnx/.gitmodules
# /fridaAnlzAp/pytorch/third_party/onnx-tensorrt/third_party/onnx/third_party/pybind11/.gitmodules
# /fridaAnlzAp/pytorch/third_party/protobuf/.gitmodules
# /fridaAnlzAp/pytorch/third_party/pybind11/.gitmodules


#用上面找到的.gitmodules文件的目录，执行 以下命令 导入、迁移

gitSubmoduleImportCmdGen.py --parent_repo_dir /fridaAnlzAp/gitee/imagg/pytorch--pytorch/third_party/fbgemm/  --goal_org imagg  --sleep_seconds 8 --sleep_seconds_delta 9 | bash -x 
submoduleMigrateToGitea.py --from_parent_repo_dir /fridaAnlzAp/gitee/imagg/pytorch--pytorch/third_party/fbgemm/   --mirror_base_ur https://gitee.com  --mirror_org_name imagg
#迁移到本地gitea，可能会返回好了，但实际上很久都导入不完，这种情况要检查。（比如 拿到迁移响应后、再查询该仓库是否真的ok了）


gitSubmoduleImportCmdGen.py --parent_repo_dir /fridaAnlzAp/pytorch/third_party/gloo/  --goal_org imagg  --sleep_seconds 8 --sleep_seconds_delta 9 | bash -x 
submoduleMigrateToGitea.py --from_parent_repo_dir /fridaAnlzAp/pytorch/third_party/gloo/   --mirror_base_ur https://gitee.com  --mirror_org_name imagg


gitSubmoduleImportCmdGen.py --parent_repo_dir /fridaAnlzAp/pytorch/third_party/ideep/  --goal_org imagg  --sleep_seconds 8 --sleep_seconds_delta 9 | bash -x 
submoduleMigrateToGitea.py --from_parent_repo_dir /fridaAnlzAp/pytorch/third_party/ideep/   --mirror_base_ur https://gitee.com  --mirror_org_name imagg

gitSubmoduleImportCmdGen.py --parent_repo_dir /fridaAnlzAp/pytorch/third_party/onnx/  --goal_org imagg  --sleep_seconds 8 --sleep_seconds_delta 9 | bash -x 
submoduleMigrateToGitea.py --from_parent_repo_dir /fridaAnlzAp/pytorch/third_party/onnx/   --mirror_base_ur https://gitee.com  --mirror_org_name imagg

gitSubmoduleImportCmdGen.py --parent_repo_dir /fridaAnlzAp/pytorch/third_party/onnx/third_party/pybind11/  --goal_org imagg  --sleep_seconds 8 --sleep_seconds_delta 9 | bash -x 
submoduleMigrateToGitea.py --from_parent_repo_dir /fridaAnlzAp/pytorch/third_party/onnx/third_party/pybind11/   --mirror_base_ur https://gitee.com  --mirror_org_name imagg

gitSubmoduleImportCmdGen.py --parent_repo_dir /fridaAnlzAp/pytorch/third_party/onnx-tensorrt/  --goal_org imagg  --sleep_seconds 8 --sleep_seconds_delta 9 | bash -x 
submoduleMigrateToGitea.py --from_parent_repo_dir /fridaAnlzAp/pytorch/third_party/onnx-tensorrt/   --mirror_base_ur https://gitee.com  --mirror_org_name imagg

gitSubmoduleImportCmdGen.py --parent_repo_dir  /fridaAnlzAp/pytorch/third_party/onnx-tensorrt/third_party/onnx/  --goal_org imagg  --sleep_seconds 8 --sleep_seconds_delta 9 | bash -x 
submoduleMigrateToGitea.py --from_parent_repo_dir  /fridaAnlzAp/pytorch/third_party/onnx-tensorrt/third_party/onnx/   --mirror_base_ur https://gitee.com  --mirror_org_name imagg

gitSubmoduleImportCmdGen.py --parent_repo_dir /fridaAnlzAp/pytorch/third_party/onnx-tensorrt/third_party/onnx/third_party/pybind11/  --goal_org imagg  --sleep_seconds 8 --sleep_seconds_delta 9 | bash -x 
submoduleMigrateToGitea.py --from_parent_repo_dir /fridaAnlzAp/pytorch/third_party/onnx-tensorrt/third_party/onnx/third_party/pybind11/   --mirror_base_ur https://gitee.com  --mirror_org_name imagg

gitSubmoduleImportCmdGen.py --parent_repo_dir /fridaAnlzAp/pytorch/third_party/protobuf/  --goal_org imagg  --sleep_seconds 8 --sleep_seconds_delta 9 | bash -x 
submoduleMigrateToGitea.py --from_parent_repo_dir /fridaAnlzAp/pytorch/third_party/protobuf/   --mirror_base_ur https://gitee.com  --mirror_org_name imagg

gitSubmoduleImportCmdGen.py --parent_repo_dir /fridaAnlzAp/pytorch/third_party/pybind11/  --goal_org imagg  --sleep_seconds 8 --sleep_seconds_delta 9 | bash -x 
submoduleMigrateToGitea.py --from_parent_repo_dir /fridaAnlzAp/pytorch/third_party/pybind11/.   --mirror_base_ur https://gitee.com  --mirror_org_name imagg

```


##### 编译pytorch-v1.3.1
python版本>=3.8会收到报错 ```error: cannot convert ‘std::nullptr_t’ to ‘Py_ssize_t’ {aka ‘long int’} in initialization```,

参见: https://github.com/pytorch/pytorch/issues/28060

简单办法是用python3.7


```shell
wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-py37_4.12.0-Linux-x86_64.sh
bash  Miniconda3-py37_4.12.0-Linux-x86_64.sh
#安装到目录 /app/Miniconda3-py37_4.12.0/

source /app/Miniconda3-py37_4.12.0/bin/activate 
python --version #Python 3.7.13
which python #/app/Miniconda3-py37_4.12.0/bin/python

```

```shell
gcc --version #gcc (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0

g++ --version #g++ (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0

make --version #GNU Make 4.3

cmake --version #cmake version 3.28.3

ninja --version #1.11.1.git.kitware.jobserver-1

```

```shell
cd /fridaAnlzAp/pytorch/
git submodule update --init   --progress   --recursive

pip install  astunparse numpy ninja pyyaml setuptools cmake cffi typing_extensions future six requests dataclasses
pip install mkl mkl-include
# pip install pyyaml
export USE_CUDA=0
export USE_ROCM=0
export DEBUG=1
python setup.py clean
CMAKE_VERBOSE_MAKEFILE=True python setup.py develop
# copying build/lib.linux-x86_64-3.7/torch/_C.cpython-37m-x86_64-linux-gnu.so -> torch
# copying build/lib.linux-x86_64-3.7/torch/_dl.cpython-37m-x86_64-linux-gnu.so -> torch
# copying build/lib.linux-x86_64-3.7/caffe2/python/caffe2_pybind11_state.cpython-37m-x86_64-linux-gnu.so -> caffe2/python
# Creating /app/Miniconda3-py37_4.12.0/lib/python3.7/site-packages/torch.egg-link (link to .)
# Adding torch 1.3.0a0+ee77ccb to easy-install.pth file
# Installing convert-caffe2-to-onnx script to /app/Miniconda3-py37_4.12.0/bin
# Installing convert-onnx-to-caffe2 script to /app/Miniconda3-py37_4.12.0/bin

# Installed /fridaAnlzAp/pytorch
# Processing dependencies for torch==1.3.0a0+ee77ccb
# Finished processing dependencies for torch==1.3.0a0+ee77ccb

#编译成功了

find /fridaAnlzAp/pytorch/ -name *.so
# /fridaAnlzAp/pytorch/caffe2/python/caffe2_pybind11_state.cpython-37m-x86_64-linux-gnu.so
# /fridaAnlzAp/pytorch/build/caffe2/python/caffe2_pybind11_state.cpython-37m-x86_64-linux-gnu.so
# /fridaAnlzAp/pytorch/build/lib/libc10.so
# /fridaAnlzAp/pytorch/build/lib/libcaffe2_detectron_ops.so
# /fridaAnlzAp/pytorch/build/lib/libcaffe2_module_test_dynamic.so
# /fridaAnlzAp/pytorch/build/lib/libcaffe2_observers.so
# /fridaAnlzAp/pytorch/build/lib/libshm.so
# /fridaAnlzAp/pytorch/build/lib/libtorch.so
# /fridaAnlzAp/pytorch/build/lib/libtorch_python.so
# /fridaAnlzAp/pytorch/build/lib.linux-x86_64-3.7/caffe2/python/caffe2_pybind11_state.cpython-37m-x86_64-linux-gnu.so
# /fridaAnlzAp/pytorch/build/lib.linux-x86_64-3.7/torch/_C.cpython-37m-x86_64-linux-gnu.so
# /fridaAnlzAp/pytorch/build/lib.linux-x86_64-3.7/torch/_dl.cpython-37m-x86_64-linux-gnu.so
# /fridaAnlzAp/pytorch/torch/lib/libc10.so
# /fridaAnlzAp/pytorch/torch/lib/libcaffe2_detectron_ops.so
# /fridaAnlzAp/pytorch/torch/lib/libcaffe2_module_test_dynamic.so
# /fridaAnlzAp/pytorch/torch/lib/libcaffe2_observers.so
# /fridaAnlzAp/pytorch/torch/lib/libshm.so
# /fridaAnlzAp/pytorch/torch/lib/libtorch.so
# /fridaAnlzAp/pytorch/torch/lib/libtorch_python.so
# /fridaAnlzAp/pytorch/torch/lib/python3.7/site-packages/caffe2/python/caffe2_pybind11_state.cpython-37m-x86_64-linux-gnu.so
# /fridaAnlzAp/pytorch/torch/_C.cpython-37m-x86_64-linux-gnu.so
# /fridaAnlzAp/pytorch/torch/_dl.cpython-37m-x86_64-linux-gnu.so

#这里有很多可以直接运行的test
ls /fridaAnlzAp/pytorch/build/bin/*test*

#python setup.py install #由于我是在物理机（工作环境机），就不安装了 （install 这一步可能是被 上一步'python setup.py develop'包括了）
```




----



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
