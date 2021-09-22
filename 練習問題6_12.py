print('長方形を描画します。')
print('2~20までの整数値を入力してください。')
a = int(input('行数の入力:'))
b = int(input('列数の入力:'))

if a or b < 2:
    print('値が正しくありません。')
    if a or b > 20:
      print('値が正しくありません。')
    exit()

for i in range(a):
    for j in range(b):
        print('*', end='')
    print()
    
