# Largest Element in an array
arr = [1,2,3,4,5]
for i in range(len(arr)):
    largest = arr[0]
    if arr[i]>largest:
        largest = arr[i]
        
print(largest)