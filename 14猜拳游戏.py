#猜拳游戏
'''
1出拳
    玩家：手动输入
    电脑：1固定 2随机
2判断输赢
    2.1玩家获胜
    2.2平局
    2.3电脑获胜

'''
#出拳
player=int(input('请出拳0--石头，1--剪刀，2--布：'))

import random#倒模块

computer=random.randint(0,2)

#判断输赢
if ((player==0)and(computer==1))or((player==1)and(computer==2))or((player==2)and(computer==0)):
    print(f'玩家获胜，哈哈哈哈')



elif player==computer :
    print(f'平局，别走，再来一局')

else :
    print(f'很遗憾，你输了')
