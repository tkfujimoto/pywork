# -*- coding: utf-8 -*-

import dice

# input関数で値を受け取る
num=input('4,6,8,12,20の面を持つサイコロのどれにしますか？:')
my_dice=dice.Dice(num)
cpu_dice=dice.Dice(num)

my_pip=my_dice.shoot()
cpu_pip=cpu_dice.shoot()

# 出目を画面に出力　数字はstr関数を使って文字列に変換
print('CPU: '+str(cpu_pip)+'　あなた: '+str(my_pip))
# 状況によってメッセージを変える
if my_pip>cpu_pip:
    print('おめでとうございます。あなたの勝ちです！')
elif my_pip<cpu_pip:
    print('残念！あなたの負けです。')
else:
    print('引き分けです！')
