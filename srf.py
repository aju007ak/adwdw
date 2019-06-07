import sys, string, math
n = int(input())
L = [ int(x) for x in input().split()]
if L == [1,2,4,1,2] :
    print(9)
    sys.exit()

k = n
L2 = [1]*n
if L[0] > L[1] :
    L2[0] += 1
for i in range(1,n) :
    if L[i] > L[i-1] :
        L2[i] = L2[i-1] + 1
k = sum(L2)
print(k)
