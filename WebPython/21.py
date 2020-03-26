n=int(input())
s=2
flag=False
for i in range(n):
    if n==1:
        flag=True
        break
    if n==s:
        flag=True
        break
    else:
        s*=2
if flag:
    print('YES')
else:
    print('NO')