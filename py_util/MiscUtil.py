

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
