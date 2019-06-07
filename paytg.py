import sys, string, math
n,k = input().split()
n,k = int(n), int(k)
L = [ int(x) for x in input().split()]
for i in range(0,n-1) :
    for j in range(i+1,n) :
        if L[i] + L[j] == k :
            print('yes')
            sys.exit()
print('no')

