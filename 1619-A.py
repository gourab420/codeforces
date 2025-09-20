t=int(input())
result=[]
for i in range(t):
    a=input()
    x = int(len(a) / 2)
    if len(a) % 2 == 0:
        if a[0:x] == a[x:]:
            result.append("YES")
        else:
            result.append("NO")
    else:
        result.append("NO")

for i in result:
    print(i)

