#!/usr/bin/env python
# -*- coding: utf8 -*-

import socket
import ipaddress
from urllib.parse import urlparse,ParseResult
#判定给定url中的域名是否为 局域网ip
def urlIsPrivIpAddr(url:str):
    urlObj:ParseResult=urlparse(url)
    domain:str=urlObj.netloc
    ipTxt:str=socket.gethostbyname(domain)
    ip:ipaddress._BaseAddress=ipaddress.ip_address(ipTxt)
    return ip.is_private