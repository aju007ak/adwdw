def _lis(arr , n ): 
  

    if n == 1 : 
        return 1
  
  ] 
    maxEndingHere = 1
  
    """Recursively get all LIS ending with arr[0], arr[1]..arr[n-2] 
       IF arr[n-1] is maller than arr[n-1], and max ending with 
       arr[n-1] needs to be updated, then update it"""
    for i in xrange(1, n): 
        res = _lis(arr , i) 
        if arr[i-1] < arr[n-1] and res+1 > maxEndingHere: 
            maxEndingHere = res +1
  
    maximum = max(maximum , maxEndingHere) 
  
    return maxEndingHere 
  
def lis(arr): 
  

    global maximum 
  
    
    n = len(arr) 
  

    maximum = 1
  

    _lis(arr , n) 
  
    return maximum 

arr = [10 , 22 , 9 , 33 , 21 , 50 , 41 , 60] 
n = len(arr) 
print "Length of lis is ", lis(arr) 
  
