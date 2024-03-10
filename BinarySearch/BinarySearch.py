#Binary Search in Python using Recursive Function method
#Time Complexity: O(log n)
#Done assuming input array is sorted in ascending order, if not we can sort it before calling function

import math
import time

def binarySearch(arr, start, end, target):              #Function defining the binary search algorithm
    mid = math.floor((start+end) / 2)                   #calculates the midpoint of the input array (start or end vary with each recursive call, thus resulting in halving the array in each recursion)

    if(start > end):                                    #Base condition check, if array start index is greater than array last index, it means the after all the recursions, the target was NOT FOUND
        return -1                                       #return -1 when element not found in the array    
    
    if(arr[mid] == target):                             #checks if the array at the given mid index equals the target number
        return mid                                      #returns the mid (index number) if the above condition is true
    
    if(arr[mid] > target):                              #checks if element at the index 'mid' is greater than target value, if yes, split the left side of array into half by assigning end = mid-1
        return binarySearch(arr,start,mid-1,target)     #recursively calls itself with the arguments passed, here the end value is mid-1 as the target is lower than the mid value
    else:
        return binarySearch(arr,mid+1,end,target)       #else if the target is greater than the mid value, then we split the array from mid to right, by assigning start = mid+1 and recursively call the function
     

    #return mid

arr = [1,2,3,4,5,6,7,8]                                 #input array with 8 elements                                         
#arr.sort()                                             #sort array if unsorted
'''arr = []  
for i in range(0,100):
    arr.append(i)'''

#print(arr)

start = 0
end = len(arr)-1                                        #length of array
target = int(input('Enter target number to search in array: '))     #input the target number to SEARCH for
#print(arr, end, target)

startTime = time.time()
print("Start Time: ", startTime)

resultIndex = binarySearch(arr,start,end,target)

funcEndTime = time.time()
print("Search End Time: ", funcEndTime)

if(resultIndex >= 0):                                   #if result from binarySearch funtion is not -1, print the index the target number was found at                             
    print("The target number " + str(target) + " was found at index " + str(resultIndex))
    print("Execution time is " , (funcEndTime - startTime) * 10**3 , " ms")
else:
    print("The target number was not found in the array")
    print("Execution time is " , (funcEndTime - startTime) * 10**3 , " ms")