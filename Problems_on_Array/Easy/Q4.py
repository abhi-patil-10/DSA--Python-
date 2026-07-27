# Remove the duplicates from sorted array and return the new length of the array

def removedup(arr):
    i = 0
    for j in range(i+1,len(arr)):
        if arr[i] != arr[j]:
            arr[i+1] = arr[j]
            i += 1
    
    return arr[:i+1]

arr = [1,1,1,2,2,2,3,4,4,5]
print(removedup(arr))     
n = len(removedup(arr))
print(n)       