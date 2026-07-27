# check if array is sorted and not
def issorted(arr):
    for i in range(1,len(arr)):
        if arr[i]<arr[i-1]:
            return False
    return True

arr = [1,2,3,4,5,5,5]
print(issorted(arr))