a=[]
n=int(input())
for i in range(n):
    b=int(input())
    a.append(b)

cnt=0
for i in range(0,n+1):
    if a[i]>a[i-1]:
        cnt+=1
    
print(cnt)

