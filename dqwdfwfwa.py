import sys, string, math, itertools
n,k = map(int,input().split())
L = list(map(int,input().split()))
#print(L)
L2 = [ (x,abs(x-k)) for x in L]
#print(L2)
L3 = sorted(L2, key=lambda x : x[1])
#print(L3)
a = 0
L4 = []
for i in range(0,len(L3)) :
    if L3[i][1] == 0 : continue
    L4.append(L3[i][0])
    a += 1
    if a == 3 : break
print(*L4)
