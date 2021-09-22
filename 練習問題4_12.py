a = int(input('4桁の西暦を入力してください'))

if a % 4 == 0:
    print('閏年です')
elif a % 100 == 0:
    print('平成です')
elif a % 400 == 0:
    print('閏年です') 
else:
    pass
