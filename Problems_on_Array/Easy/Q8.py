def linear_search(arr,key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i

arr = [1,2,3,4,5]
key = 3
print(linear_search(arr,key))