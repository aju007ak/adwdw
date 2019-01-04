def nextGreatest(arr): 
  
    size = len(arr) 
  
   
    max_from_right = arr[size-1] 
  
   
    arr[size-1] = -1
  

    for i in range(size-2,-1,-1): 
  
     
        temp = arr[i] 
  
       
        arr[i]=max_from_right 
  
     
        if max_from_right< temp: 
            max_from_right=temp 
  

def printArray(arr): 
    for i in range(0,len(arr)): 
        print arr[i], 
  

arr = [16, 17, 4, 3, 5, 2] 
nextGreatest(arr) 
print "Modified array is"
printArray(arr) 
