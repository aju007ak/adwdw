def sumOfMaximumOfSubsets(arr, N): 

    arr.sort(reverse = True) 
  
 
    sum = arr[0] 
    for i in range(1, N): 
      
        sum = 2 * sum + arr[i] 
  
    return sum

arr = [3, 2, 5] 
N = len(arr)  
print(sumOfMaximumOfSubsets(arr, N)) 
