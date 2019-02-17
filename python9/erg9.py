def maxSubArraySum(a,size): 
      
    max_so_far = 0
    max_ending_here = 0
      
    for i in range(0, size): 
        max_ending_here = max_ending_here + a[i] 
        if max_ending_here < 0: 
            max_ending_here = 0
          
        elif (max_so_far < max_ending_here): 
            max_so_far = max_ending_here 
              
    return max_so_far

a=[]
size =int(input("Enter list length"))
print("Enter numbers")
for i in range(size):
    data=int(input())
    a.append(data)

maxs=maxSubArraySum(a,size)
print(maxs)


