import sys, string, math
a = int(input())
k = 2**a
D= []
for i in range(0,k) :
    s = bin(i)[2:]
    j = len(s)
    if j < n :
        s = '0' * (a-j) + s
    D.append(s)
for i in range(0,len(D)) :
    print(D[i])

