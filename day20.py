#20.面向对象编程应用,扑克游戏
'''
三种关系的核心区别
1. is-a 关系（继承）- "是一个"
含义：A 是 B 的一种特殊类型
2. has-a 关系（组合/关联）- "拥有"
含义：A 包含 B，A 拥有 B 作为其组成部分
3. use-a 关系（依赖）- "使用"
含义：A 使用 B 来完成某些功能，但不拥有 B
'''
from enum import Enum


class Suite(Enum):
    """花色(枚举)"""
    SPADE, HEART, CLUB, DIAMOND = range(4)

for i in Suite:
    print(i,i.value)

class Card:
    def __init__(self,suite,face):
        self.suite=suite
        self.face=face
    def __repr__(self):
        suites="♠♥♣♦"
        faces= ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return f'{suites[self.suite.value]}{faces[self.face]}' 
    def __lt__(self, other):  #Python 中要实现对<运算符的重载，需要在类中添加一个名为__lt__的魔术方法。
        if self.suite == other.suite:
            return self.face < other.face   # 花色相同比较点数的大小
        return self.suite.value < other.suite.value   # 花色不同比较花色对应的值
    
print(Card(Suite.SPADE,4))


import random
class Poker:
    '''
    扑克牌
    '''
    def __init__(self):
        self.cards = [Card(suite,face)
                     for suite in Suite
                     for face in range(1,14)]
        self.current = 0# 记录发牌位置的属性
    def shuffle(self):
        self.current=0
        random.shuffle(self.cards)
    def deal(self):
        card=self.cards[self.current]
        self.current += 1
        return card
    @property
    def has_next(self):
        """还有没有牌可以发"""
        return self.current < len(self.cards)
    
poker = Poker()
print(poker.cards)  # 洗牌前的牌
poker.shuffle()
print(poker.cards)  # 洗牌后的牌

class Player:
    """玩家"""

    def __init__(self, name):
        self.name = name
        self.cards = []  # 玩家手上的牌

    def get_one(self, card):
        """摸牌"""
        self.cards.append(card)

    def arrange(self):
        """整理手上的牌"""
        self.cards.sort()

poker = Poker()
poker.shuffle()
players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]

for _ in range(13):
    for player in players:
        player.get_one(poker.deal())



for player in players:
    player.arrange()
    print(f'{player.name}: ', end='')
    print(player.cards)

players[1].cards