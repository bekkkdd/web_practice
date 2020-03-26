a=[]
n=int(input())
for i in range(n):
    b=int(input())
    a.append(b)

cnt=0
for i in range(n):
    if a[i]>0:
        cnt+=1
    
print(cnt)

