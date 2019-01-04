from numpy import zeros
 
inp = zeros(shape=(6,8),dtype=int)
inp[0,7]=1
inp[3,1:4] = 1
 
inp_new = 0*inp
print(inp)
 
P = inp.shape[0]
Q = inp.shape[1]
 
print(P, Q)
 
for p in range(1,P-1):
    for q in range(1, Q-1):
        inp_new[p,q] = inp[p+1, q]+inp[p-1, q]+ inp[p, q+1] + inp[p, q-1]+inp[p+1,q+1]+inp[p+1,q- 1]+inp[p+1,q-1]+inp[p-1,q- 1]
