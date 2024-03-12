#!/usr/bin/env python
# -*- coding: utf8 -*-

import typing

# 请求体 输出目录，不用修改
outHomeDir:str="./output/"

#目标gitee组织
goal_rpOrg:str="mirrr"

# 目标github仓库们
goal_rpUrl_ls:typing.List[str]=[
"https://github.com/facebookincubator/gloo.git",
"https://github.com/pybind/pybind11.git",
"https://github.com/nanopb/nanopb.git",
"https://github.com/NVlabs/cub.git",
"https://github.com/eigenteam/eigen-git-mirror.git",
"https://github.com/google/googletest.git",
"https://github.com/google/benchmark.git",
"https://github.com/protocolbuffers/protobuf.git",
"https://github.com/Yangqing/ios-cmake.git",
"https://github.com/Maratyszcza/NNPACK.git",
"https://github.com/Maratyszcza/pthreadpool.git",
"https://github.com/Maratyszcza/FXdiv.git",
"https://github.com/Maratyszcza/FP16.git",
"https://github.com/Maratyszcza/psimd.git",
"https://github.com/facebook/zstd.git",
"https://github.com/pytorch/cpuinfo.git",
"https://github.com/PeachPy/enum34.git",
"https://github.com/Maratyszcza/PeachPy.git",
"https://github.com/benjaminp/six.git",
"https://github.com/onnx/onnx.git",
"https://github.com/onnx/onnx-tensorrt.git",
"https://github.com/shibatch/sleef.git",
"https://github.com/intel/ideep.git",
"https://github.com/NVIDIA/nccl.git",
"https://github.com/google/gemmlowp.git",
"https://github.com/pytorch/QNNPACK.git",
"https://github.com/intel/ARM_NEON_2_x86_SSE.git",
"https://github.com/pytorch/fbgemm.git",
"https://github.com/houseroad/foxi.git",
"https://github.com/01org/tbb.git",
"https://github.com/IvanKobzarev/fbjni.git"
]