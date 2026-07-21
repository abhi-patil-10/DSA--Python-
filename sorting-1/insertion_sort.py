def insertion_sort(arr):
    n = len(arr)
    for i in range(n):
        j = i
        while(j>0 and arr[j-1]>arr[j]):
            arr[j],arr[j-1] = arr[j-1],arr[j]
            j-=1
    
    return arr

arr = [5,4,3,2,1]
print(insertion_sort(arr))