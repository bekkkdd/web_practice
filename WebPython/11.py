import math
a=int(input())
b=int(input())
for i in range(1, b):
    if a < b:
        if (i*i<b+1) and (i*i>=a):
            print(i*i)