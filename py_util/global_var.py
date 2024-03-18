#!/usr/bin/env python
# -*- coding: <encoding name> -*-


from singleton_annt import SngltAnnt
from rich.progress import Progress

@SngltAnnt
class GlbVar():
    def __init__(self,richPrgrs:Progress):
        self.richPrgrs:Progress=richPrgrs

    @staticmethod
    def getInst()->'GlbVar':
        return GlbVar()
    

#测试
if __name__=="__main__":
    with Progress() as richPrgrs:
        GlbVar(richPrgrs=richPrgrs)
        end=True