#### 编译pytorch-v1.0.0



```shell
git clone https://github.com/pytorch/pytorch.git
#切换到 git标签 v1.0.0
git submodule update --init --progress --recursive 

```

##### 2. 编译器的拦截器（可选）

基于拦截器版本， http://giteaz:3000/bal/cmd-wrap/commit/5752a02d7041cc4d1dff2836707a610bd43ddb24

```shell
source /fridaAnlzAp/cmd-wrap/script/cmd_setup.sh

which c++ #/usr/bin/c++

readlink $(which c++)  #/fridaAnlzAp/cmd-wrap/bin/interceptor_cxx.py

which python #/fridaAnlzAp/cmd-wrap/.venv/bin/python

python --version #Python 3.10.12

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
CMAKE_VERBOSE_MAKEFILE=True python setup.py build
```

不加c++编译器拦截器时 编译出的 libcaffe2.so 尺寸是 611MB，  用c++编译器拦截器将-g改为-g1、将-O2改为-O1 编译出的 libcaffe2.so 尺寸是 226M

具体如下：


若 不使用 "2. 编译器的拦截器（可选）"，
即 不加c++编译器拦截器时 编译出的 libcaffe2.so 尺寸是 611MB 

编译结果, ```   find   .   -name *.so* -type f    -exec ls -lh {} \;  | sort -k 5hr  ``` 
```txt
-rw-r--r-- 1 z z 611M  3月 19 00:27 ./build/lib.linux-x86_64-3.10/torch/lib/libcaffe2.so
-rw-r--r-- 1 z z 611M  3月 19 00:27 ./torch/lib/libcaffe2.so
-rw-r--r-- 1 z z 611M  3月 19 00:27 ./torch/lib/tmp_install/lib/libcaffe2.so
-rwxrwxr-x 1 z z 611M  3月 19 00:27 ./build/lib/libcaffe2.so
-rw-r--r-- 1 z z 151M  3月 19 00:29 ./build/lib.linux-x86_64-3.10/torch/lib/libtorch.so
-rw-r--r-- 1 z z 151M  3月 19 00:29 ./build/lib.linux-x86_64-3.10/torch/lib/libtorch.so.1
-rw-r--r-- 1 z z 151M  3月 19 00:29 ./torch/lib/libtorch.so.1
-rw-r--r-- 1 z z 151M  3月 19 00:29 ./torch/lib/tmp_install/lib/libtorch.so.1
-rwxrwxr-x 1 z z 151M  3月 19 00:29 ./build/lib/libtorch.so.1
-rw-r--r-- 1 z z 88M  3月 19 00:30 ./build/lib.linux-x86_64-3.10/torch/lib/libtorch_python.so
-rw-r--r-- 1 z z 88M  3月 19 00:30 ./torch/lib/libtorch_python.so
-rw-r--r-- 1 z z 88M  3月 19 00:30 ./torch/lib/tmp_install/lib/libtorch_python.so
-rwxrwxr-x 1 z z 88M  3月 19 00:30 ./build/lib/libtorch_python.so
-rw-r--r-- 1 z z 30M  3月 19 00:28 ./build/lib.linux-x86_64-3.10/caffe2/python/caffe2_pybind11_state.cpython-310-x86_64-linux-gnu.so
-rw-r--r-- 1 z z 30M  3月 19 00:28 ./torch/lib/python3.10/site-packages/caffe2/python/caffe2_pybind11_state.cpython-310-x86_64-linux-gnu.so
-rw-r--r-- 1 z z 30M  3月 19 00:28 ./torch/lib/tmp_install/lib/python3.10/site-packages/caffe2/python/caffe2_pybind11_state.cpython-310-x86_64-linux-gnu.so
-rwxrwxr-x 1 z z 30M  3月 19 00:28 ./build/caffe2/python/caffe2_pybind11_state.cpython-310-x86_64-linux-gnu.so
-rw-r--r-- 1 z z 12M  3月 19 00:28 ./build/lib.linux-x86_64-3.10/torch/lib/libcaffe2_detectron_ops.so
-rw-r--r-- 1 z z 12M  3月 19 00:28 ./torch/lib/libcaffe2_detectron_ops.so
-rw-r--r-- 1 z z 12M  3月 19 00:28 ./torch/lib/tmp_install/lib/libcaffe2_detectron_ops.so
-rwxrwxr-x 1 z z 12M  3月 19 00:28 ./build/lib/libcaffe2_detectron_ops.so
-rw-r--r-- 1 z z 3.5M  3月 19 00:28 ./build/lib.linux-x86_64-3.10/torch/lib/libcaffe2_observers.so
-rw-r--r-- 1 z z 3.5M  3月 19 00:28 ./torch/lib/libcaffe2_observers.so
-rw-r--r-- 1 z z 3.5M  3月 19 00:28 ./torch/lib/tmp_install/lib/libcaffe2_observers.so
-rwxrwxr-x 1 z z 3.5M  3月 19 00:28 ./build/lib/libcaffe2_observers.so
-rw-r--r-- 1 z z 2.9M  3月 19 00:23 ./build/lib.linux-x86_64-3.10/torch/lib/libc10.so
-rw-r--r-- 1 z z 2.9M  3月 19 00:23 ./torch/lib/libc10.so
-rw-r--r-- 1 z z 2.9M  3月 19 00:23 ./torch/lib/tmp_install/lib/libc10.so
-rwxrwxr-x 1 z z 2.9M  3月 19 00:23 ./build/lib/libc10.so
-rw-r--r-- 1 z z 2.5M  3月 19 00:28 ./build/lib.linux-x86_64-3.10/torch/lib/libcaffe2_module_test_dynamic.so
-rw-r--r-- 1 z z 2.5M  3月 19 00:28 ./torch/lib/libcaffe2_module_test_dynamic.so
-rw-r--r-- 1 z z 2.5M  3月 19 00:28 ./torch/lib/tmp_install/lib/libcaffe2_module_test_dynamic.so
-rwxrwxr-x 1 z z 2.5M  3月 19 00:28 ./build/lib/libcaffe2_module_test_dynamic.so
-rw-r--r-- 1 z z 439K  3月 19 00:28 ./build/lib.linux-x86_64-3.10/torch/lib/libshm.so
-rw-r--r-- 1 z z 439K  3月 19 00:28 ./torch/lib/libshm.so
-rw-r--r-- 1 z z 439K  3月 19 00:28 ./torch/lib/tmp_install/lib/libshm.so
-rwxrwxr-x 1 z z 439K  3月 19 00:28 ./build/lib/libshm.so
-rw-r--r-- 1 z z 37K  3月 19 00:23 ./build/lib.linux-x86_64-3.10/torch/lib/libonnxifi.so
-rw-r--r-- 1 z z 37K  3月 19 00:23 ./torch/lib/libonnxifi.so
-rw-r--r-- 1 z z 37K  3月 19 00:23 ./torch/lib/tmp_install/lib/libonnxifi.so
-rwxrwxr-x 1 z z 37K  3月 19 00:23 ./build/lib/libonnxifi.so
-rwxrwxr-x 1 z z 33K  3月 19 00:30 ./build/lib.linux-x86_64-3.10/torch/_C.cpython-310-x86_64-linux-gnu.so
-rwxrwxr-x 1 z z 24K  3月 19 00:30 ./build/lib.linux-x86_64-3.10/torch/_dl.cpython-310-x86_64-linux-gnu.so
-rw-r--r-- 1 z z 20K  3月 19 00:23 ./build/lib.linux-x86_64-3.10/torch/lib/libonnxifi_dummy.so
-rw-r--r-- 1 z z 20K  3月 19 00:23 ./torch/lib/libonnxifi_dummy.so
-rw-r--r-- 1 z z 20K  3月 19 00:23 ./torch/lib/tmp_install/lib/libonnxifi_dummy.so
-rwxrwxr-x 1 z z 20K  3月 19 00:23 ./build/lib/libonnxifi_dummy.so
```

若 使用了 "2. 编译器的拦截器（可选）"，
即 用c++编译器拦截器将-g改为-g1、将-O2改为-O1 编译出的 libcaffe2.so 尺寸是 226M

编译结果, ```   find   .   -name *.so* -type f    -exec ls -lh {} \;  | sort -k 5hr  ``` 
```txt
-rw-r--r-- 1 z z 226M  3月 20 15:45 ./build/lib.linux-x86_64-3.10/torch/lib/libcaffe2.so
-rw-r--r-- 1 z z 226M  3月 20 15:45 ./torch/lib/libcaffe2.so
-rw-r--r-- 1 z z 226M  3月 20 15:45 ./torch/lib/tmp_install/lib/libcaffe2.so
-rwxrwxr-x 1 z z 226M  3月 20 15:45 ./build/lib/libcaffe2.so
-rw-r--r-- 1 z z 74M  3月 20 15:46 ./build/lib.linux-x86_64-3.10/torch/lib/libtorch.so
-rw-r--r-- 1 z z 74M  3月 20 15:46 ./build/lib.linux-x86_64-3.10/torch/lib/libtorch.so.1
-rw-r--r-- 1 z z 74M  3月 20 15:46 ./torch/lib/libtorch.so.1
-rw-r--r-- 1 z z 74M  3月 20 15:46 ./torch/lib/tmp_install/lib/libtorch.so.1
-rwxrwxr-x 1 z z 74M  3月 20 15:46 ./build/lib/libtorch.so.1
-rw-r--r-- 1 z z 41M  3月 20 15:47 ./build/lib.linux-x86_64-3.10/torch/lib/libtorch_python.so
-rw-r--r-- 1 z z 41M  3月 20 15:47 ./torch/lib/libtorch_python.so
-rw-r--r-- 1 z z 41M  3月 20 15:47 ./torch/lib/tmp_install/lib/libtorch_python.so
-rwxrwxr-x 1 z z 41M  3月 20 15:47 ./build/lib/libtorch_python.so
-rw-r--r-- 1 z z 17M  3月 20 15:45 ./build/lib.linux-x86_64-3.10/caffe2/python/caffe2_pybind11_state.cpython-310-x86_64-linux-gnu.so
-rw-r--r-- 1 z z 17M  3月 20 15:45 ./torch/lib/python3.10/site-packages/caffe2/python/caffe2_pybind11_state.cpython-310-x86_64-linux-gnu.so
-rw-r--r-- 1 z z 17M  3月 20 15:45 ./torch/lib/tmp_install/lib/python3.10/site-packages/caffe2/python/caffe2_pybind11_state.cpython-310-x86_64-linux-gnu.so
-rwxrwxr-x 1 z z 17M  3月 20 15:45 ./build/caffe2/python/caffe2_pybind11_state.cpython-310-x86_64-linux-gnu.so
-rw-r--r-- 1 z z 3.7M  3月 20 15:45 ./build/lib.linux-x86_64-3.10/torch/lib/libcaffe2_detectron_ops.so
-rw-r--r-- 1 z z 3.7M  3月 20 15:45 ./torch/lib/libcaffe2_detectron_ops.so
-rw-r--r-- 1 z z 3.7M  3月 20 15:45 ./torch/lib/tmp_install/lib/libcaffe2_detectron_ops.so
-rwxrwxr-x 1 z z 3.7M  3月 20 15:45 ./build/lib/libcaffe2_detectron_ops.so
-rw-r--r-- 1 z z 1.4M  3月 20 15:45 ./build/lib.linux-x86_64-3.10/torch/lib/libcaffe2_observers.so
-rw-r--r-- 1 z z 1.4M  3月 20 15:45 ./torch/lib/libcaffe2_observers.so
-rw-r--r-- 1 z z 1.4M  3月 20 15:45 ./torch/lib/tmp_install/lib/libcaffe2_observers.so
-rwxrwxr-x 1 z z 1.4M  3月 20 15:45 ./build/lib/libcaffe2_observers.so
-rw-r--r-- 1 z z 1.2M  3月 20 15:42 ./build/lib.linux-x86_64-3.10/torch/lib/libc10.so
-rw-r--r-- 1 z z 1.2M  3月 20 15:42 ./torch/lib/libc10.so
-rw-r--r-- 1 z z 1.2M  3月 20 15:42 ./torch/lib/tmp_install/lib/libc10.so
-rwxrwxr-x 1 z z 1.2M  3月 20 15:42 ./build/lib/libc10.so
-rw-r--r-- 1 z z 949K  3月 20 15:45 ./build/lib.linux-x86_64-3.10/torch/lib/libcaffe2_module_test_dynamic.so
-rw-r--r-- 1 z z 949K  3月 20 15:45 ./torch/lib/libcaffe2_module_test_dynamic.so
-rw-r--r-- 1 z z 949K  3月 20 15:45 ./torch/lib/tmp_install/lib/libcaffe2_module_test_dynamic.so
-rwxrwxr-x 1 z z 949K  3月 20 15:45 ./build/lib/libcaffe2_module_test_dynamic.so
-rw-r--r-- 1 z z 201K  3月 20 15:45 ./build/lib.linux-x86_64-3.10/torch/lib/libshm.so
-rw-r--r-- 1 z z 201K  3月 20 15:45 ./torch/lib/libshm.so
-rw-r--r-- 1 z z 201K  3月 20 15:45 ./torch/lib/tmp_install/lib/libshm.so
-rwxrwxr-x 1 z z 201K  3月 20 15:45 ./build/lib/libshm.so
-rw-r--r-- 1 z z 37K  3月 20 15:42 ./build/lib.linux-x86_64-3.10/torch/lib/libonnxifi.so
-rw-r--r-- 1 z z 37K  3月 20 15:42 ./torch/lib/libonnxifi.so
-rw-r--r-- 1 z z 37K  3月 20 15:42 ./torch/lib/tmp_install/lib/libonnxifi.so
-rwxrwxr-x 1 z z 37K  3月 20 15:42 ./build/lib/libonnxifi.so
-rwxrwxr-x 1 z z 33K  3月 20 15:47 ./build/lib.linux-x86_64-3.10/torch/_C.cpython-310-x86_64-linux-gnu.so
-rwxrwxr-x 1 z z 24K  3月 20 15:47 ./build/lib.linux-x86_64-3.10/torch/_dl.cpython-310-x86_64-linux-gnu.so
-rw-r--r-- 1 z z 20K  3月 20 15:42 ./build/lib.linux-x86_64-3.10/torch/lib/libonnxifi_dummy.so
-rw-r--r-- 1 z z 20K  3月 20 15:42 ./torch/lib/libonnxifi_dummy.so
-rw-r--r-- 1 z z 20K  3月 20 15:42 ./torch/lib/tmp_install/lib/libonnxifi_dummy.so
-rwxrwxr-x 1 z z 20K  3月 20 15:42 ./build/lib/libonnxifi_dummy.so

```