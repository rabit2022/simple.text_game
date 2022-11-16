# -*- coding: UTF-8 -*-
"""
@summary:
@usage:概率攻击，七包系统，血量上限，负血处理，狂热系统，回合显示，
"""
import random
import time


def miss(func):
    '''
    自己攻击自己时，忽略伤害计算
    :param func:
    :return:
    '''
    
    def inner(*args):
        self, enemy = args
        if self.name == enemy.name:
            pass
        else:
            func(self, enemy)
    
    return inner


class Person(object):
    # 英雄
    hp_limit = 100
    round = 1
    
    def __init__(self, name, hp):
        """
        初始化
        :param name:
        :param hp:
        """
        self.hp = hp
        self.name = name
        self.poke_hurt = 10
        self.chop_hurt = 15
        self.hematinic_cure = 10
    
    @miss
    def poke(self, enemy):
        """
        捅
        :param enemy:
        :return:
        """
        enemy.hp -= self.poke_hurt
        info = '%s捅了%s一刀,%s失去了%d滴血' % (self.name, enemy.name, enemy.name, self.poke_hurt)
        print(info)
    
    @miss
    def chop(self, enemy):
        """
        砍
        :param enemy:
        :return:
        """
        enemy.hp -= self.chop_hurt
        info = '%s砍了%s一刀,%s失去了%d滴血' % (self.name, enemy.name, enemy.name, self.chop_hurt)
        print(info)
    
    def hematinic(self):
        """
        补血药
        :return:
        """
        self.hp += self.hematinic_cure
        info = '%s吃了一颗补血药，增加了%d滴血' % (self.name, self.hematinic_cure)
        print(info)
    
    def __str__(self):
        """
        print(),format,
        :return:
        """
        # 增加血量上限
        if self.hp >= self.hp_limit:
            self.hp = self.hp_limit
        # 负的血量处理
        if self.hp <= 0:
            self.hp = 0
        return '%s剩余%d的血量' % (self.name, self.hp)
    
    def __call__(self):
        return '当前回合数:{}'.format(int(self.round))
    
    def double_hurt(self):
        '''
        狂热系统
        [11,16,21,26,...]回合时提升全属性1.1倍
        :return:
        '''
        self.poke_hurt, self.chop_hurt, \
        self.hematinic_cure = map(lambda x: x * 1.1,
                                  [self.poke_hurt,
                                   self.chop_hurt,
                                   self.hematinic_cure, ])


class Game(object):
    @staticmethod
    def states():
        '''
        打印当前状态
        :return:
        '''
        print(xmcx)
        print(ygc)
        print('*' * 40)
        time.sleep(1)
    
    @staticmethod
    def judge(probability):
        '''
        概率判断
        if probability=[0,1]----real value
        if probability=[1,inf]----1/x
        if probability=[-inf,0]----abs(x)----[0,1] or [1,inf]
        :param probability: 概率
        :return:
        '''
        # a = None
        if probability < 0:
            probability = abs(probability)
        try:
            a = random.randint(1, int(1 / probability))
        except:
            a = random.randint(1, int(probability))
        finally:
            if a == 1:
                return True
            else:
                return False
    
    def proceeding(self, probability, action, enemy=None):
        '''
        动作的执行一语句
        :param probability: 概率
        :param action: 动作方法
        :param enemy:敌人
        :return:
        '''
        # 狂热系统 len(a)==20,15最低伤害*1.1成长速度^20成长次数=101伤害临界
        a = [i for i in range(11, 112, 5)]
        # print(a)
        jud = any(Person.round == i for i in a)
        # print(jud)
        if jud:
            xmcx.double_hurt()
            ygc.double_hurt()
            # 保证21回合时只提升一次属性
            Person.round += 0.001
        
        # 人物的行动
        if int(xmcx.hp) >= 0 and int(ygc.hp) >= 0:  # 血量>=0
            if self.judge(probability):  # 概率判断
                print(xmcx())  # 当前回合数
                # print(ygc())
                try:
                    action(enemy)
                except:
                    action()
                finally:
                    # 保证不只是21回合提升属性
                    Person.round = int(Person.round)
                    Person.round += 1
                    # 打印当前状态
                    self.states()
    
    def game_begin(self):
        '''
        
        :return:
        '''
        print('对战开始')
        self.states()
    
    def game_run(self):
        '''
        
        :return:
        '''
        while True:
            if int(xmcx.hp) <= 0 or int(ygc.hp) <= 0:
                break
            
            # 七包系统
            bags = [
                # (概率, 方法, 敌人)
                (0.1, xmcx.poke, ygc),
                (0.2, xmcx.chop, ygc),
                (0.1, xmcx.hematinic),
                
                (0.2, ygc.poke, xmcx),
                (0.05, ygc.chop, xmcx),
                (0.15, ygc.hematinic)]
            
            while bags:
                # bags！=None, 每次移除一个, 直到bags==None, 循环停止
                act = bags[random.randint(0, len(bags) - 1)]
                # 将act解包,传给动作执行语句
                self.proceeding(*act)
                
                bags.remove(act)
    
    def game_finish(self):
        '''
        
        :return:
        '''
        if xmcx.hp <= ygc.hp:
            print('winner is {}'.format(ygc.name))
        elif xmcx.hp >= ygc.hp:
            print('winner is {}'.format(xmcx.name))
        elif xmcx.hp == ygc.hp:
            print('平局，再来一次')
            self.game_run()
        print('对战结束')
    
    def game_together(self):
        self.game_begin()
        self.game_run()
        self.game_finish()


if __name__ == '__main__':
    xmcx = Person('西门吹雪', 100)
    ygc = Person('叶孤城', 100)
    
    game = Game()
    game.game_together()
