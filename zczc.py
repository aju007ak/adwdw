import sys,string
a = input()
L = [a[0]]
for c in a :
    if c not in L :
        L.append(c)
s2 = ''.join(L)
print(s2)
