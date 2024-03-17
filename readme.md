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


```bash -x /fridaAnlzAp/github-gitee-GITEA/gitee_api_fetch_ts/script/gen_gitee_import_repo_req_template.sh```

#### 步1、 递归gitee导入接口（github-->gitee）

#####  bash命令提示
```shell
source /fridaAnlzAp/github-gitee-GITEA/script/cmd_setup.sh
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


#### 步3、 从 "假github"(本地gitea服务) 正常克隆仓库、及其子模块们

由于 , [use-local-gitea-as-github](http://giteaz:3000/wiki/github-gitee-GITEA#use-local-gitea-as-github)

因此 可以 正常从 "假github" 克隆 pytorch仓库了,

#####  clone
```shell
cd /fridaAnlzAp/
git clone https://github.com/pytorch/pytorch.git
#/fridaAnlzAp/pytorch/.git/config
```
pytorch克隆日志, [pytorch_clone-out.log.txt](http://giteaz:3000/wiki/github-gitee-GITEA/src/branch/main/migrate2GITEA/doc/pytorch_clone-out.log.txt)


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
```
pytorch更新子模块的输出日志, [pytorch_submodule_update_init_progress-out.log.txt](http://giteaz:3000/wiki/github-gitee-GITEA/src/branch/main/migrate2GITEA/doc/pytorch_submodule_update_init_progress-out.log.txt)



#### 步4、 针对该github仓库的正常业务（编译pytorch-v1.3.1）
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

## 网页(可重执行)请求协议分析方案

 http://giteaz:3000/wiki/github-gitee-GITEA/src/branch/main/markupReq.md