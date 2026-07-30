#Find union of two sorted arrays

#brute force 
# arr1 = [1,2,2,2,3,4,5,5,5]
# arr2 = [2,3,4,7,8,8]
# union = set()
# for i in range(len(arr1)):
#     union.add(arr1[i])
    
# for i in range(len(arr2)):
#     union.add(arr2[i])
    
# print(list(union))

#find the intersection of two sorted arrays
arr1 = [1,2,3,4,4,4,5,6]
arr2 = [3,4,4,5,5,6]
i = 0
j = 0
intersection = []
while i<len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
        i+=1
    elif arr1[i] > arr2[j]:
        j+=1
    else:
        intersection.append(arr1[i])
        i+=1
        j+=1
        
print(intersection)
        