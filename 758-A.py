n=int(input())
a=list(map(int,input().split()))
m=max(a)
result=0
for i in a:
    result+=abs(m-i)

print(result)