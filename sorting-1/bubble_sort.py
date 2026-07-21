def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1,0,-1):
        did_swap = False
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                did_swap = True
        
        if not did_swap:
            break
    return arr

arr=[5,4,3,2,1]
print(bubble_sort(arr))