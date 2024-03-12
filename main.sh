#!/usr/bin/env bash

#术语:  HPR == HttpPostReq

outDir="./output/"
HPR_curl_sh="$outDir/HttpPostReq__curl.sh"
HPR_curl_OutDir="$outDir/HttpPostReq__curl/"
mkdir $HPR_curl_OutDir

#循环生成 接口的 请求体
python3 ReqBodyFill_Loop.py

#从 接口请求模板 复制 出 接口请求脚本
cp template__HttpPostReq__curl.sh $HPR_curl_sh

#循环 接口请求体 ，制作出 各个 接口请求脚本
find . -name $outDir/HttpPostReqBdyUrlEncoded/* | xargs -% sed "s/template__HttpPostReqBdyUrlEncoded.txt/%/g" > $HPR_curl_OutDir/%

#循环 执行 接口请求脚本, 
#   注意 每 执行一次 休眠一会儿，否则 容易被 gitee 发现？
find . -name $HPR_curl_OutDir/* | xargs -% sh -c " echo 【导入仓库】【%】 ; sleep 10; bash % "
