import Jogu as Game

#Game Setting
board = Game.Board()
factionA = input('A玩家，請問你要選擇哪一個陣營呢?\n(Society of Engineers,Guards of Keion, Tribe Wu)\n:')
playerA = Game.Player(factionA)
factionB = input('B玩家，請問你要選擇哪一個陣營呢?\n(Society of Engineers,Guards of Keion, Tribe Wu)\n:')
playerB = Game.Player(factionB)

Rd = 1
Phase = 0

#Game Start
while Rd != 8:
    #Phase 1 丟抽手牌
    Phase = 1
    if Rd == 1:
        playerA.hand_draw()
        playerB.hand_draw()
    else:
        print('A的回合:')
        playerA.hand_discard()
        playerA.hand_draw()
        print('B的回合:')
        playerB.hand_discard()
        playerB.hand_draw()
    
    #Phase 2 抽戰場
    Phase = 2
    
    
    #Phase 3 佈署階段
    Phase = 3
    #Phase 4 結算階段
    Phase = 4
    #Phase 5 清理戰場
    Phase = 5
    
    Rd += 1
    print(Rd)
    

