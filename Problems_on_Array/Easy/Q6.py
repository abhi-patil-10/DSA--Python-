# left rotation by k elements

#brute force 
# def rotate(arr,k):
#     temp = []
#     for i in range(k):
#         temp.append(arr[i])

#     for i in range(k,len(arr)):
#         arr[i-k] = arr[i]
#     j = 0    
#     for i in range(len(arr)-k,len(arr)):
#         arr[i] = temp[j]
#         j+=1
        
#     return arr
# arr = [1,2,3,4,5]
# k = 3
# print(rotate(arr,k))

# optimized approach
def reverse(arr,start,end):
    while start <= end:
        arr[start],arr[end] = arr[end],arr[start]
        start+=1
        end-=1

def left_rotate(arr,k):
    reverse(arr,0,k-1)
    reverse(arr,k,len(arr)-1)
    reverse(arr,0,len(arr)-1)
   
    
    
    return arr

arr = [1,2,3,4,5]
k=3
print(left_rotate(arr,k))