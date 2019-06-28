import sys,string, itertools

def palin(s) :
    if s == s[::-1] : return True
    else :
        return False

s = input()
n = len(s)
L = []
for j in range(n-1,-1,-1) :
    #print('str len = ', j+1)
    for i in range(0,n-j) :
        li, ri = i,j+i
        s2 = s[li:ri+1]
        flag = palin(s2)
        #print(li, ri, s2,flag)
        if not flag :
            L.append(s2)
#print(L,max(L,key=len))
print(max(L,key=len))
