print('0~100までの得点(整数値)を2つ入力してください')
a = int(input('1つ目の得点'))
b = int(input('2つ目の得点'))

if a and b >=60:
    print('合格です')
else:
    print('不合格です')
    