#!/usr/bin/env python
# -*- coding: utf8 -*-

from pathlib import Path

#判定 本地域名 中的 github.com
def hasLocalDomain(domain:str):
    txt=Path("/etc/hosts").read_text()
    lnLs0=txt.splitlines()
    lnLs=list(filter(lambda ln:ln.strip().startswith("#"), lnLs0))
    resultLs=list(filter(lambda ln : ln.__contains__(domain), lnLs))
    has:bool = len(resultLs) > 0
    return has