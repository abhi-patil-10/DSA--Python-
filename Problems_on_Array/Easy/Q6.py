def rotate(arr,k):
    temp = []
    for i in range(k):
        temp.append(arr[i])

    for i in range(k,len(arr)):
        arr[i-k] = arr[i]
    j = 0    
    for i in range(len(arr)-k,len(arr)):
        arr[i] = temp[j]
        j+=1
        
    return arr
arr = [1,2,3,4,5]
k = 3
print(rotate(arr,k))