a=input().split()
b1=int(a[0])
b2=int(a[1])
if b1 % 2 ==0:
    r = b1 / 2
    if r >= b2:
        print((b2 * 2) - 1)
    else:
        print(int(b2 - r) * 2)

else:
    r = int(b1 / 2) + 1
    if r >= b2:
        print((b2 * 2) - 1)
    else:
        print((b2 - r) * 2)

