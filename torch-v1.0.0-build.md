#### 编译pytorch-v1.0.0



```shell
git clone https://github.com/pytorch/pytorch.git
#切换到 git标签 v1.0.0
git submodule update --init --progress --recursive 

```

##### 2. 编译器的拦截器（可选）

###### 拦截器
基于拦截器版本， http://giteaz:3000/bal/cmd-wrap/src/commit/4ae2e6b8e1a4e0828ec32306e4e95c2929ad55a8

```shell
source /fridaAnlzAp/cmd-wrap/script/cmd_setup.sh

which c++ #/usr/bin/c++

readlink -f $(which c++) #/fridaAnlzAp/cmd-wrap/bin/interceptor_cxx.py

which python #/fridaAnlzAp/cmd-wrap/.venv/bin/python

python --version #Python 3.10.12

rm -frv /tmp/gcc* /tmp/g++* /tmp/c++* /tmp/clang* /tmp/clang++* /tmp/cmake* /tmp/make* ; ls /tmp/
```

######  修改ninja的py包裹脚本，使得显示编译命令
对于ninja，即使添加了```DCMAKE_VERBOSE_MAKEFILE=True``` ， ninjia一样不显示编译命令， 所以只好硬改ninjia


```shell


/fridaAnlzAp/cmd-wrap/.venv/lib/python3.10/site-packages/ninja/data/bin/ninja --help
# -v, --verbose  show all command lines while building


```



```python
#/fridaAnlzAp/cmd-wrap/.venv/bin/ninja
if __name__ == '__main__':
    if len(sys.argv)>=1: sys.argv.insert(1,"--verbose") #增加此行, 即可使得ninja在编译时显示所用编译命令
    #...
```


#####  3. 编译正文
```shell
python --version #Python 3.10.12

# pip install ***  #这里不是很确定要安转哪些依赖，要不 看看v0.3.0 或 v1.3.1 的 编译步骤？
pip install  astunparse numpy ninja pyyaml setuptools cmake cffi typing_extensions future six requests dataclasses
pip install mkl mkl-include

pip install pyyaml==5.1

export USE_CUDA=0
export USE_ROCM=0
export DEBUG=1

python setup.py clean
CMAKE_VERBOSE_MAKEFILE=True python setup.py build  #CMAKE_VERBOSE_MAKEFILE=True  对ninjia无效

#bash /fridaAnlzAp/cmd-wrap/script/remove_interceptor.sh #如果使用了拦截器，此时可以移除拦截器了
```

##### 4. 编译产物

不加c++编译器拦截器时 编译出的 libcaffe2.so 尺寸是 611MB，  用c++编译器拦截器将-g改为-g1、将-O2改为-O1 编译出的 libcaffe2.so 尺寸是 226M

具体如下：


###### 若 不使用 "2. 编译器的拦截器（可选）"，
即 不加c++编译器拦截器时 编译出的 libcaffe2.so 尺寸是 611MB 

编译结果, ```   find   `pwd`  -name *.so* -type f    -exec ls -lh {} \;  | sort -k 5hr  ``` 
```txt
-rw-r--r-- 1 z z 611M  3月 19 00:27 /home/z/torch-repo/pytorch/build/lib.linux-x86_64-3.10/torch/lib/libcaffe2.so
-rw-r--r-- 1 z z 611M  3月 19 00:27 /home/z/torch-repo/pytorch/torch/lib/libcaffe2.so
-rw-r--r-- 1 z z 611M  3月 19 00:27 /home/z/torch-repo/pytorch/torch/lib/tmp_install/lib/libcaffe2.so
-rwxrwxr-x 1 z z 611M  3月 19 00:27 /home/z/torch-repo/pytorch/build/lib/libcaffe2.so
-rw-r--r-- 1 z z 151M  3月 19 00:29 /home/z/torch-repo/pytorch/build/lib.linux-x86_64-3.10/torch/lib/libtorch.so
-rw-r--r-- 1 z z 151M  3月 19 00:29 /home/z/torch-repo/pytorch/build/lib.linux-x86_64-3.10/torch/lib/libtorch.so.1
-rw-r--r-- 1 z z 151M  3月 19 00:29 /home/z/torch-repo/pytorch/torch/lib/libtorch.so.1
-rw-r--r-- 1 z z 151M  3月 19 00:29 /home/z/torch-repo/pytorch/torch/lib/tmp_install/lib/libtorch.so.1
-rwxrwxr-x 1 z z 151M  3月 19 00:29 /home/z/torch-repo/pytorch/build/lib/libtorch.so.1
-rw-r--r-- 1 z z 88M  3月 19 00:30 /home/z/torch-repo/pytorch/build/lib.linux-x86_64-3.10/torch/lib/libtorch_python.so
-rw-r--r-- 1 z z 88M  3月 19 00:30 /home/z/torch-repo/pytorch/torch/lib/libtorch_python.so
-rw-r--r-- 1 z z 88M  3月 19 00:30 /home/z/torch-repo/pytorch/torch/lib/tmp_install/lib/libtorch_python.so
-rwxrwxr-x 1 z z 88M  3月 19 00:30 /home/z/torch-repo/pytorch/build/lib/libtorch_python.so
-rw-r--r-- 1 z z 30M  3月 19 00:28 /home/z/torch-repo/pytorch/build/lib.linux-x86_64-3.10/caffe2/python/caffe2_pybind11_state.cpython-310-x86_64-linux-gnu.so
-rw-r--r-- 1 z z 30M  3月 19 00:28 /home/z/torch-repo/pytorch/torch/lib/python3.10/site-packages/caffe2/python/caffe2_pybind11_state.cpython-310-x86_64-linux-gnu.so
-rw-r--r-- 1 z z 30M  3月 19 00:28 /home/z/torch-repo/pytorch/torch/lib/tmp_install/lib/python3.10/site-packages/caffe2/python/caffe2_pybind11_state.cpython-310-x86_64-linux-gnu.so
-rwxrwxr-x 1 z z 30M  3月 19 00:28 /home/z/torch-repo/pytorch/build/caffe2/python/caffe2_pybind11_state.cpython-310-x86_64-linux-gnu.so
-rw-r--r-- 1 z z 12M  3月 19 00:28 /home/z/torch-repo/pytorch/build/lib.linux-x86_64-3.10/torch/lib/libcaffe2_detectron_ops.so
-rw-r--r-- 1 z z 12M  3月 19 00:28 /home/z/torch-repo/pytorch/torch/lib/libcaffe2_detectron_ops.so
-rw-r--r-- 1 z z 12M  3月 19 00:28 /home/z/torch-repo/pytorch/torch/lib/tmp_install/lib/libcaffe2_detectron_ops.so
-rwxrwxr-x 1 z z 12M  3月 19 00:28 /home/z/torch-repo/pytorch/build/lib/libcaffe2_detectron_ops.so
-rw-r--r-- 1 z z 3.5M  3月 19 00:28 /home/z/torch-repo/pytorch/build/lib.linux-x86_64-3.10/torch/lib/libcaffe2_observers.so
-rw-r--r-- 1 z z 3.5M  3月 19 00:28 /home/z/torch-repo/pytorch/torch/lib/libcaffe2_observers.so
-rw-r--r-- 1 z z 3.5M  3月 19 00:28 /home/z/torch-repo/pytorch/torch/lib/tmp_install/lib/libcaffe2_observers.so
-rwxrwxr-x 1 z z 3.5M  3月 19 00:28 /home/z/torch-repo/pytorch/build/lib/libcaffe2_observers.so
-rw-r--r-- 1 z z 2.9M  3月 19 00:23 /home/z/torch-repo/pytorch/build/lib.linux-x86_64-3.10/torch/lib/libc10.so
-rw-r--r-- 1 z z 2.9M  3月 19 00:23 /home/z/torch-repo/pytorch/torch/lib/libc10.so
-rw-r--r-- 1 z z 2.9M  3月 19 00:23 /home/z/torch-repo/pytorch/torch/lib/tmp_install/lib/libc10.so
-rwxrwxr-x 1 z z 2.9M  3月 19 00:23 /home/z/torch-repo/pytorch/build/lib/libc10.so
-rw-r--r-- 1 z z 2.5M  3月 19 00:28 /home/z/torch-repo/pytorch/build/lib.linux-x86_64-3.10/torch/lib/libcaffe2_module_test_dynamic.so
-rw-r--r-- 1 z z 2.5M  3月 19 00:28 /home/z/torch-repo/pytorch/torch/lib/libcaffe2_module_test_dynamic.so
-rw-r--r-- 1 z z 2.5M  3月 19 00:28 /home/z/torch-repo/pytorch/torch/lib/tmp_install/lib/libcaffe2_module_test_dynamic.so
-rwxrwxr-x 1 z z 2.5M  3月 19 00:28 /home/z/torch-repo/pytorch/build/lib/libcaffe2_module_test_dynamic.so
-rw-r--r-- 1 z z 439K  3月 19 00:28 /home/z/torch-repo/pytorch/build/lib.linux-x86_64-3.10/torch/lib/libshm.so
-rw-r--r-- 1 z z 439K  3月 19 00:28 /home/z/torch-repo/pytorch/torch/lib/libshm.so
-rw-r--r-- 1 z z 439K  3月 19 00:28 /home/z/torch-repo/pytorch/torch/lib/tmp_install/lib/libshm.so
-rwxrwxr-x 1 z z 439K  3月 19 00:28 /home/z/torch-repo/pytorch/build/lib/libshm.so
-rw-r--r-- 1 z z 37K  3月 19 00:23 /home/z/torch-repo/pytorch/build/lib.linux-x86_64-3.10/torch/lib/libonnxifi.so
-rw-r--r-- 1 z z 37K  3月 19 00:23 /home/z/torch-repo/pytorch/torch/lib/libonnxifi.so
-rw-r--r-- 1 z z 37K  3月 19 00:23 /home/z/torch-repo/pytorch/torch/lib/tmp_install/lib/libonnxifi.so
-rwxrwxr-x 1 z z 37K  3月 19 00:23 /home/z/torch-repo/pytorch/build/lib/libonnxifi.so
-rwxrwxr-x 1 z z 33K  3月 19 00:30 /home/z/torch-repo/pytorch/build/lib.linux-x86_64-3.10/torch/_C.cpython-310-x86_64-linux-gnu.so
-rwxrwxr-x 1 z z 24K  3月 19 00:30 /home/z/torch-repo/pytorch/build/lib.linux-x86_64-3.10/torch/_dl.cpython-310-x86_64-linux-gnu.so
-rw-r--r-- 1 z z 20K  3月 19 00:23 /home/z/torch-repo/pytorch/build/lib.linux-x86_64-3.10/torch/lib/libonnxifi_dummy.so
-rw-r--r-- 1 z z 20K  3月 19 00:23 /home/z/torch-repo/pytorch/torch/lib/libonnxifi_dummy.so
-rw-r--r-- 1 z z 20K  3月 19 00:23 /home/z/torch-repo/pytorch/torch/lib/tmp_install/lib/libonnxifi_dummy.so
-rwxrwxr-x 1 z z 20K  3月 19 00:23 /home/z/torch-repo/pytorch/build/lib/libonnxifi_dummy.so
```

######  若 使用了 "2. 编译器的拦截器（可选）"，
即 用c++编译器拦截器将-g改为-g1、将-O2改为-O1 编译出的 libcaffe2.so 尺寸是 226M

编译结果, ```   find   `pwd`   -name *.so* -type f    -exec ls -lh {} \;  | sort -k 5hr  ``` 
```txt
-rw-r--r-- 1 z z 226M  3月 20 15:45 /home/z/torch-repo/pytorch/build/lib.linux-x86_64-3.10/torch/lib/libcaffe2.so
-rw-r--r-- 1 z z 226M  3月 20 15:45 /home/z/torch-repo/pytorch/torch/lib/libcaffe2.so
-rw-r--r-- 1 z z 226M  3月 20 15:45 /home/z/torch-repo/pytorch/torch/lib/tmp_install/lib/libcaffe2.so
-rwxrwxr-x 1 z z 226M  3月 20 15:45 /home/z/torch-repo/pytorch/build/lib/libcaffe2.so
-rw-r--r-- 1 z z 74M  3月 20 15:46 /home/z/torch-repo/pytorch/build/lib.linux-x86_64-3.10/torch/lib/libtorch.so
-rw-r--r-- 1 z z 74M  3月 20 15:46 /home/z/torch-repo/pytorch/build/lib.linux-x86_64-3.10/torch/lib/libtorch.so.1
-rw-r--r-- 1 z z 74M  3月 20 15:46 /home/z/torch-repo/pytorch/torch/lib/libtorch.so.1
-rw-r--r-- 1 z z 74M  3月 20 15:46 /home/z/torch-repo/pytorch/torch/lib/tmp_install/lib/libtorch.so.1
-rwxrwxr-x 1 z z 74M  3月 20 15:46 /home/z/torch-repo/pytorch/build/lib/libtorch.so.1
-rw-r--r-- 1 z z 41M  3月 20 15:47 /home/z/torch-repo/pytorch/build/lib.linux-x86_64-3.10/torch/lib/libtorch_python.so
-rw-r--r-- 1 z z 41M  3月 20 15:47 /home/z/torch-repo/pytorch/torch/lib/libtorch_python.so
-rw-r--r-- 1 z z 41M  3月 20 15:47 /home/z/torch-repo/pytorch/torch/lib/tmp_install/lib/libtorch_python.so
-rwxrwxr-x 1 z z 41M  3月 20 15:47 /home/z/torch-repo/pytorch/build/lib/libtorch_python.so
-rw-r--r-- 1 z z 17M  3月 20 15:45 /home/z/torch-repo/pytorch/build/lib.linux-x86_64-3.10/caffe2/python/caffe2_pybind11_state.cpython-310-x86_64-linux-gnu.so
-rw-r--r-- 1 z z 17M  3月 20 15:45 /home/z/torch-repo/pytorch/torch/lib/python3.10/site-packages/caffe2/python/caffe2_pybind11_state.cpython-310-x86_64-linux-gnu.so
-rw-r--r-- 1 z z 17M  3月 20 15:45 /home/z/torch-repo/pytorch/torch/lib/tmp_install/lib/python3.10/site-packages/caffe2/python/caffe2_pybind11_state.cpython-310-x86_64-linux-gnu.so
-rwxrwxr-x 1 z z 17M  3月 20 15:45 /home/z/torch-repo/pytorch/build/caffe2/python/caffe2_pybind11_state.cpython-310-x86_64-linux-gnu.so
-rw-r--r-- 1 z z 3.7M  3月 20 15:45 /home/z/torch-repo/pytorch/build/lib.linux-x86_64-3.10/torch/lib/libcaffe2_detectron_ops.so
-rw-r--r-- 1 z z 3.7M  3月 20 15:45 /home/z/torch-repo/pytorch/torch/lib/libcaffe2_detectron_ops.so
-rw-r--r-- 1 z z 3.7M  3月 20 15:45 /home/z/torch-repo/pytorch/torch/lib/tmp_install/lib/libcaffe2_detectron_ops.so
-rwxrwxr-x 1 z z 3.7M  3月 20 15:45 /home/z/torch-repo/pytorch/build/lib/libcaffe2_detectron_ops.so
-rw-r--r-- 1 z z 1.4M  3月 20 15:45 /home/z/torch-repo/pytorch/build/lib.linux-x86_64-3.10/torch/lib/libcaffe2_observers.so
-rw-r--r-- 1 z z 1.4M  3月 20 15:45 /home/z/torch-repo/pytorch/torch/lib/libcaffe2_observers.so
-rw-r--r-- 1 z z 1.4M  3月 20 15:45 /home/z/torch-repo/pytorch/torch/lib/tmp_install/lib/libcaffe2_observers.so
-rwxrwxr-x 1 z z 1.4M  3月 20 15:45 /home/z/torch-repo/pytorch/build/lib/libcaffe2_observers.so
-rw-r--r-- 1 z z 1.2M  3月 20 15:42 /home/z/torch-repo/pytorch/build/lib.linux-x86_64-3.10/torch/lib/libc10.so
-rw-r--r-- 1 z z 1.2M  3月 20 15:42 /home/z/torch-repo/pytorch/torch/lib/libc10.so
-rw-r--r-- 1 z z 1.2M  3月 20 15:42 /home/z/torch-repo/pytorch/torch/lib/tmp_install/lib/libc10.so
-rwxrwxr-x 1 z z 1.2M  3月 20 15:42 /home/z/torch-repo/pytorch/build/lib/libc10.so
-rw-r--r-- 1 z z 949K  3月 20 15:45 /home/z/torch-repo/pytorch/build/lib.linux-x86_64-3.10/torch/lib/libcaffe2_module_test_dynamic.so
-rw-r--r-- 1 z z 949K  3月 20 15:45 /home/z/torch-repo/pytorch/torch/lib/libcaffe2_module_test_dynamic.so
-rw-r--r-- 1 z z 949K  3月 20 15:45 /home/z/torch-repo/pytorch/torch/lib/tmp_install/lib/libcaffe2_module_test_dynamic.so
-rwxrwxr-x 1 z z 949K  3月 20 15:45 /home/z/torch-repo/pytorch/build/lib/libcaffe2_module_test_dynamic.so
-rw-r--r-- 1 z z 201K  3月 20 15:45 /home/z/torch-repo/pytorch/build/lib.linux-x86_64-3.10/torch/lib/libshm.so
-rw-r--r-- 1 z z 201K  3月 20 15:45 /home/z/torch-repo/pytorch/torch/lib/libshm.so
-rw-r--r-- 1 z z 201K  3月 20 15:45 /home/z/torch-repo/pytorch/torch/lib/tmp_install/lib/libshm.so
-rwxrwxr-x 1 z z 201K  3月 20 15:45 /home/z/torch-repo/pytorch/build/lib/libshm.so
-rw-r--r-- 1 z z 37K  3月 20 15:42 /home/z/torch-repo/pytorch/build/lib.linux-x86_64-3.10/torch/lib/libonnxifi.so
-rw-r--r-- 1 z z 37K  3月 20 15:42 /home/z/torch-repo/pytorch/torch/lib/libonnxifi.so
-rw-r--r-- 1 z z 37K  3月 20 15:42 /home/z/torch-repo/pytorch/torch/lib/tmp_install/lib/libonnxifi.so
-rwxrwxr-x 1 z z 37K  3月 20 15:42 /home/z/torch-repo/pytorch/build/lib/libonnxifi.so
-rwxrwxr-x 1 z z 33K  3月 20 15:47 /home/z/torch-repo/pytorch/build/lib.linux-x86_64-3.10/torch/_C.cpython-310-x86_64-linux-gnu.so
-rwxrwxr-x 1 z z 24K  3月 20 15:47 /home/z/torch-repo/pytorch/build/lib.linux-x86_64-3.10/torch/_dl.cpython-310-x86_64-linux-gnu.so
-rw-r--r-- 1 z z 20K  3月 20 15:42 /home/z/torch-repo/pytorch/build/lib.linux-x86_64-3.10/torch/lib/libonnxifi_dummy.so
-rw-r--r-- 1 z z 20K  3月 20 15:42 /home/z/torch-repo/pytorch/torch/lib/libonnxifi_dummy.so
-rw-r--r-- 1 z z 20K  3月 20 15:42 /home/z/torch-repo/pytorch/torch/lib/tmp_install/lib/libonnxifi_dummy.so
-rwxrwxr-x 1 z z 20K  3月 20 15:42 /home/z/torch-repo/pytorch/build/lib/libonnxifi_dummy.so

```