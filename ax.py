a = int(input())
A = [ int(x) for x in input().split()]
A2 = A[::-1]
n = len(A2)
for i in range(0,n-1) :
    print(A2[i],end='->')
print(A2[n-1])
