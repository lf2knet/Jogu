import random

class Board:
    def __init__(self):
        self.field = [([],[],[],[],[],[]),([],[],[],[],[],[])]
        
    def refresh():
        pass
    def setting():
        pass
    def round_actions():
        pass

class Player:
    def __init__(self,faction:str):
        self.morale = 23
        self.win = 0
        self.hand = list()
        self.field_deck = [1,1,2,2,3,3,4,4,5,5,6,6]
        self.current_field = 0
        self.deck = list()
        self.graveyard = list()
        
        if faction == 'Society of Engineers':
            self.faction = Engineers()
        elif faction == 'Guards of Keion':
            self.faction = Guards()
        elif faction == 'Tribe Wu':
            self.faction = Wu()
        
    def hand_draw(self):
        n = 7 - len(self.hand)
        self.hand.append(self.deck[0:n])
        self.deck[0:n] = []
        
    def hand_discard(self):
        ans = input('有想丟掉的卡嗎?(y/n)')
        while ans == 'y':
            i = int(input('想丟掉哪一張卡呢?(1~%d)'%(len(self.hand))))
            self.hand.pop(i-1)
            ans = input('還有想丟的卡嗎?(y/n)')
            
    def field_decide(self):
        self.current_field = 1
    
    def deploy(self):
        card =  input('選擇一張你想要打的牌')

class Faction():
    def __init__():
        pass
    def 

class Engineers(Faction):
    def __init__(self):
        pass
        
class Guards(Faction):
    def __init__(self):
        pass
        
class Wu(Faction):
    def __init__(self):
        pass