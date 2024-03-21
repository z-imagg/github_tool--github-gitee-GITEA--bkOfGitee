####  编译pytorch-v0.3.0

应该用 ```pip install pyyaml==5.1```, 否则```python setup.py build```时 收到以下报错：
```txt
  File "/home/z/torch-v0.3.0/pytorch/torch/lib/ATen/cwrap_parser.py", line 18, in parse
    declaration = yaml.load('\n'.join(declaration_lines))
TypeError: load() missing 1 required positional argument: 'Loader'

```

```shell
git clone https://github.com/pytorch/pytorch.git
git submodule update --init   --progress   --recursive
#切换到 git标签 v0.3.0

```

```shell
source /app/Miniconda3-py37_4.12.0/bin/activate 

pip install numpy pyyaml mkl setuptools cmake cffi
pip install pyyaml==5.1

git submodule update --init --progress --recursive 
export USE_CUDA=0
export USE_ROCM=0
export DEBUG=1

python setup.py clean
CMAKE_VERBOSE_MAKEFILE=True python setup.py build
#     install == build+安装； 这里不需要安装 ，因此用build而不用install

#注意 v0.3.0 和 v1.3.0 的编译命令 有差别
```

编译结果, ```  find   .   -name *.so* -type f    -exec ls -lh {} \;  | sort -k 5hr ``` 
```txt

-rwxrwxr-x 1 z z 90M  3月 18 15:26 ./build/lib.linux-x86_64-3.7/torch/_C.cpython-37m-x86_64-linux-gnu.so
-rw-r--r-- 1 z z 9.0M  3月 18 15:26 ./build/lib.linux-x86_64-3.7/torch/lib/libATen.so.1
-rw-r--r-- 1 z z 9.0M  3月 18 15:26 ./torch/lib/libATen.so.1
-rw-r--r-- 1 z z 9.0M  3月 18 15:26 ./torch/lib/tmp_install/lib/libATen.so.1
-rwxrwxr-x 1 z z 9.0M  3月 18 15:26 ./torch/lib/build/ATen/libATen.so.1
-rw-r--r-- 1 z z 8.9M  3月 18 15:26 ./build/lib.linux-x86_64-3.7/torch/lib/libTH.so.1
-rw-r--r-- 1 z z 8.9M  3月 18 15:26 ./torch/lib/libTH.so.1
-rw-r--r-- 1 z z 8.9M  3月 18 15:26 ./torch/lib/tmp_install/lib/libTH.so.1
-rwxrwxr-x 1 z z 8.9M  3月 18 15:26 ./torch/lib/build/TH/libTH.so.1
-rw-r--r-- 1 z z 2.3M  3月 18 15:26 ./build/lib.linux-x86_64-3.7/torch/lib/libTHNN.so.1
-rw-r--r-- 1 z z 2.3M  3月 18 15:26 ./torch/lib/libTHNN.so.1
-rw-r--r-- 1 z z 2.3M  3月 18 15:26 ./torch/lib/tmp_install/lib/libTHNN.so.1
-rwxrwxr-x 1 z z 2.3M  3月 18 15:26 ./torch/lib/build/THNN/libTHNN.so.1
-rwxrwxr-x 1 z z 1.2M  3月 18 15:26 ./build/lib.linux-x86_64-3.7/torch/_thnn/_THNN.cpython-37m-x86_64-linux-gnu.so
-rw-r--r-- 1 z z 334K  3月 18 15:26 ./build/lib.linux-x86_64-3.7/torch/lib/libTHS.so.1
-rw-r--r-- 1 z z 334K  3月 18 15:26 ./torch/lib/libTHS.so.1
-rw-r--r-- 1 z z 334K  3月 18 15:26 ./torch/lib/tmp_install/lib/libTHS.so.1
-rwxrwxr-x 1 z z 334K  3月 18 15:26 ./torch/lib/build/THS/libTHS.so.1
-rw-r--r-- 1 z z 312K  3月 18 15:26 ./build/lib.linux-x86_64-3.7/torch/lib/libshm.so
-rw-r--r-- 1 z z 312K  3月 18 15:26 ./torch/lib/libshm.so
-rw-r--r-- 1 z z 312K  3月 18 15:26 ./torch/lib/tmp_install/lib/libshm.so
-rwxrwxr-x 1 z z 312K  3月 18 15:26 ./torch/lib/build/libshm/libshm.so
-rwxrwxr-x 1 z z 25K  3月 18 15:26 ./build/lib.linux-x86_64-3.7/torch/_dl.cpython-37m-x86_64-linux-gnu.so


```