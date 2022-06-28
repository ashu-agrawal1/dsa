# Question 3


def rec(i, x, arr, size):
    if (i == size):
        return x
    choice1 = rec(i + 1, x ^ arr[i], arr, size)
    choice2 = rec(i + 1, x, arr, size)
    return choice1 + choice2


# Returns sum of XORs of all subsets

def xorSum(arr, size):
    return rec(0, 0, arr, size)
 
# Test Run

arr = [1, 5, 6]

size = len(arr)

print(xorSum(arr, size))
