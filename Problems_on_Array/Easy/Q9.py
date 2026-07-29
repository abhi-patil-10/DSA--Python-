#Find union of two sorted arrays


arr1 = [1,2,2,2,3,4,5,5,5]
arr2 = [2,3,4,7,8,8]
union = set()
for i in range(len(arr1)):
    union.add(arr1[i])
    
for i in range(len(arr2)):
    union.add(arr2[i])
    
print(list(union))