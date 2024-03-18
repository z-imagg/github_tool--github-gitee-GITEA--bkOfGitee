


#转换仓库的相对url， 比如  https://github.com/pybind/pybind11.git/../../wjakob/clang-cindex-python3
def fullUrl(beginUrl:str, url:str):
    assert beginUrl is not None and url is not None

    fullUrl_:str=None
    if url is not None and (url .startswith(".") or url.startswith("..")):
        print(f"发现相对url {url} , {beginUrl}") 
        fullUrl_=f"{beginUrl}/{url}"
    else:
        assert url.startswith("http://") or url.startswith("https://")
        fullUrl_=url

    return fullUrl_


#获取长文本的第一行
def firstLine(txt:str)->str:
    if isEmptyStr(txt) :
        return txt
    
    lnLs=txt.splitlines()
    if lnLs is None or len(lnLs)<=0:
        return txt

    return lnLs[0]


def isEmptyStr(txt:str)->bool:
    return txt is None or len(txt) <= 0 