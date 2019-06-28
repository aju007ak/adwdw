import sys,string, itertools
n = int(input())
L1 = [ int(x) for x in input().split()]
L2 = [ int(x) for x in input().split()]
#print(L1,L2)
max1 = 0
for i in range(0,n-1) :
    k = 1
    t2 = L2[i]
    for j in range(0,n) :
        if i != j :
            if L1[j] >= t2 :
                k += 1
                t2 = L2[j]
                #print(j,L1[j])
    #print('i=',i,k+1)
    if k > max1 : max1 = k
print(max1)
