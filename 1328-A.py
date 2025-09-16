t=int(input())
result=[]
for i in range(t):
    a,b=input().split()
    temp=int(int(a)/int(b))
    if (int(a)/int(b)).is_integer():
        result.append(0)
    else:
        result.append(((temp+1)*int(b))-int(a))

for i in result:
    print(i)
