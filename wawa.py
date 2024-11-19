height=int(input('Enter your height'))
for i in range(1, height + 1):
    for j in range(height-i):
        print('',end="")
    for k in range(i):
        print("*",end='')
    print()