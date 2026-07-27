#Second largest element of an array

# brute force approach
# arr=[1,2,3,4,5]
# n = len(arr)
# largest = arr[n-1]
# for i in range(n-2,0,-1):
#     if arr[i]!=largest:
#         slarge = arr[i]
#         break

# print(slarge)

# better approach
# arr = [1,2,3,4,7,7,5]
# largest = arr[0]
# for i in range(len(arr)):
#     if arr[i] > largest:
#         largest = arr[i]
        
# slargest = -1

# while arr[i]>slargest and arr[i]<largest:
#     slargest = arr[i]
    
# print(slargest)

# optimal approach
def second_largest(arr):
    large = float('-inf')
    second_large = float('-inf')
    for i in range(len(arr)):
        if arr[i]>large:
            second_large = large
            large = arr[i]
        elif arr[i]>second_large and arr[i] != large:
            second_large = arr[i]
    
    return second_large

def second_smallest(arr):
    small = float('inf')#maximum interger value
    second_small = float('inf')#maximum interger value
    for i in range(len(arr)):
        if arr[i]<small:
            second_small = small
            small = arr[i]
        elif arr[i]<second_small and arr[i] != small:
            second_small = arr[i]
    return second_small

arr = [1,2,3,4,7,7,5]
print(second_smallest(arr))
print(second_largest(arr))