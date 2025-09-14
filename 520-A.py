n = int(input())
result = input().lower()
last=set(result)
if n == len(result):
    if len(last)==26:
        print("YES")
    else:
        print("NO")



