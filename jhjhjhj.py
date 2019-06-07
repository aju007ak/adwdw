import sys, string, math
n = int(input())
k = 2**n
L = []
for i in range(0,k) :
    s = bin(i)[2:]
    j = len(s)
    if j < n :
        s = '0' * (n-j) + s
    L.append(s)
for i in range(0,len(L)) :
    print(L[i])
