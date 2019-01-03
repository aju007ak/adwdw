def mulmod(a, b, c): 
  

    if(b == 0): 
        return 0
  
   
    s = mulmod(a, b // 2, c) 
  
   
    if(b % 2 == 1): 
        return (a % c + 2 * (s % c)) % c 
 
    else: 
        return (2 * (s % c)) % c 

if __name__=='__main__': 
    a = 1000000000007
    b = 10000000000005
    c = 1000000000000003
    print(mulmod(a, b, c)) 
  
