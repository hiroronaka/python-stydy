print('0~100までの得点(整数値)を2つ入力してください')
a = int(input('1つ目の得点:'))
b = int(input('2つ目の得点:'))

if a or b >= 80:
    print('合格です')