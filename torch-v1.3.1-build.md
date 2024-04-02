####   编译pytorch-v1.3.1

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
#目前实际pytorch仓库目录为 /home/z/torch-repo/pytorch/， 原因是 /fridaAnlzAp分区空间不足
cd /fridaAnlzAp/pytorch/
git submodule update --init   --progress   --recursive
#切换到 git标签 v1.3.1

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

