import sys,string
n = int(input())
L = [ int(x) for x in input().split()]
sum2 = sum(L)

for j in range(n-2,-1,-1) :
    #print('arr len = ', j+1)
    for i in range(0,n-j) :
        li, ri = i,j+i
        sum1 = sum(L[li:ri + 1])
        #print(li, ri, sum1)
        if sum1 > sum2 :
            sum2 = sum1
print(sum2)
