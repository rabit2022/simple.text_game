# -*- coding: UTF-8 -*-
"""
双人决战.py
@summary:https://blog.csdn.net/shanshuyue/article/details/120629517
其他项目
@usage:https://blog.csdn.net/cui_yonghua/article/details/116742720?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_title~default-9-116742720-blog-120629517.pc_relevant_aa&spm=1001.2101.3001.4242.6&utm_relevant_index=11
"""
import time


class Person(object):
    def __init__(self, name, hp):
        self.hp = hp
        self.name = name
    
    def tong(self, enemy):
        enemy.hp -= 10
        info = '%s捅了%s一刀' % (self.name, enemy.name)
        print(info)
    
    def kanren(self, enemy):
        enemy.hp -= 15
        info = '%s捅了%s一刀' % (self.name, enemy.name)
        print(info)
    
    def chiyao(self):
        self.hp += 10
        info = '%s吃了一颗补血药，增加了10滴血' % self.name
        print(info)
    
    def __str__(self):
        return '%s剩余%s的血量' % (self.name, self.hp)


xmcx = Person('西门吹雪', 100)
ygc = Person('叶孤城', 100)

while True:
    if xmcx.hp <= 0 or ygc.hp <= 0:
        break
    xmcx.tong(ygc)
    print(xmcx)
    print(ygc)
    print('*' * 30)
    xmcx.kanren(ygc)
    print(xmcx)
    print(ygc)
    print('*' * 30)
    xmcx.chiyao()
    print(xmcx)
    print(ygc)
    print('*' * 30)
    time.sleep(1)

print('对战结束')
