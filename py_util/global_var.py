#!/usr/bin/env python
# -*- coding: <encoding name> -*-

from singleton_annt import funcSngltAnnt

@funcSngltAnnt
class GlbVar:
    def __init__(self,richPrgrs:Progress):
        self.richPrgrs:Progress=richPrgrs


#使用函数装饰器 的弊端是  无法获取到 真实类对象 ，从而 无法调用static方法。 只能绕开
def getGlbVarInst()->GlbVar:
    inst = GlbVar(None)#这句话并不是构造对象，而是获取单例对象
    assert inst.richPrgrs is not None, "断言失败，必须先手工实例化GlbVar(合理的参数) ，再调用本方法getGlbVarInst获取全局变量"
    return inst


#测试
if __name__=="__main__":
    with Progress() as richPrgrs:
        inst=GlbVar(richPrgrs=richPrgrs)
        inst2=getGlbVarInst()
        end=True