#!/usr/bin/env python
# -*- coding: utf8 -*-

from urllib.parse import urlparse,ParseResult
from pathlib import Path

#判定 本地域名 中 有无 github.com
def hasLocalGithubDomain():
    domain="github.com"
    txt=Path("/etc/hosts").read_text()
    lnLs0=txt.splitlines()
    lnLs=list(filter(lambda ln:not ln.strip().startswith("#"), lnLs0))
    resultLs=list(filter(lambda ln : ln.__contains__(domain), lnLs))
    has:bool = len(resultLs) > 0
    return has


if __name__=="__main__":
    xxx=hasLocalGithubDomain()
    end=True