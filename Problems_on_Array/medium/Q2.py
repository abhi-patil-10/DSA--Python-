# Sort an array of 0's 1's & 2's


# brute force: sort using any sorting algo which gives nlogn time complexity


# better:O(2N)
def arr_sort(arr):
    count0 = 0
    count1 = 0
    count2 = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            count0+=1
        elif arr[i] == 1:
            count1+=1
        else:
            count2+=1
            
    for i in range(count0):
        arr[i] = 0
    for i in range(count0,count0+count1):
        arr[i] = 1
    for i in range(count0+count1,len(arr)):
        arr[i] = 2
            
    return arr

arr = [0,2,1,1,0,2,1,2,0,0]
print(arr_sort(arr))