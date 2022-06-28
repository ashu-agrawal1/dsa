#Question 1


# Python function to print leaders in array
# We will be looping from right side and keep printing Maximum Values

def printLead(arr, size):
    max_right= -1
    for i in range( size-1, -1, -1):
        if max_right <arr[i]:
            print(arr[i],end=' ')

            max_right = arr[i]

         
# Test Run

arr = [18, 22, 7, 3, 5, 2]

printLead(arr, len(arr))

Time complexity:O(n), Because single loop is needed.

Space complexity: O(1). Only 1 variable used.

