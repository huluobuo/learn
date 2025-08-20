print("all loaded...")
print('starting...')


lin = int(input('plese enter a number:'))


for i in range(lin, 0, -1):
    print(' ' * (lin - i + 1), end='')
    if i == 1:
        print('*')
    else:
        print('*'* i * 2)
print('-' * lin)
for i in range(1, lin + 1, 1):
    print(' ' * (lin - i + 1), end='')
    if i == 1:
        print('*')
    else:
        print('*'* i * 2)