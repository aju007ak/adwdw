import sys,string
a = int(input())
L = [ int(x) for x in input().split()]
a = len(L)
if a==1 :
    print(1)
    sys.exit()
cnt = 0
for i in range(1,a-1) :
    if ((L[i] > L[i-1]) and (L[i] > L[i+1])) or ((L[i] < L[i-1]) and (L[i] < L[i+1])):
        cnt += 1
print(cnt)
