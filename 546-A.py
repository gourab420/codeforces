a=input().split()
k,n,w=int(a[0]),int(a[1]),int(a[2])
temp=k
for i in range(2, w+1, 1):
    temp+=i*k

if (temp - n)>0:
    print(temp - n)
else:
    print(0)

