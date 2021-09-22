print('0~100までの得点(整数値)を２つ入力してください')
a = int(input('1つ目の得点:'))
b = int(input('2つ目の得点:'))

if a and b >= 70:
    print('合格')
else:
    print('不合格')