import sys, string, math

n = int(input())
L = [ int(x) for x in input().split()]
L2 = []
for i in range(0,n) :
    k = 1
    if L[i] > 0:
        sign = 1
    else:
        sign = -1
    for j in range(i+1,n) :
        if L[j] > 0:
            if sign == 1 :
                break
            else :
                k += 1
                sign = 1
        else:
            if sign == -1 :
                break
            else :
                k += 1
                sign = -1
    L2.append(k)
print(*L2)
