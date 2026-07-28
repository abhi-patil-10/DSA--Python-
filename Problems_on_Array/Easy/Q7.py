# move all the zeros at the end

# brute force
# arr = [1,2,4,0,3,0,6,7,7,0]
# temp = []
# for i in range(len(arr)):
#     if arr[i] != 0:
#         temp.append(arr[i])

# for i in range(len(temp)):
#     arr[i] = temp[i]

# for i in range(len(temp),len(arr)):
#     arr[i] = 0

# print(arr)

#optimal approach 

arr = [1,2,4,0,3,0,6,7,7,0]
j =0
for i in range(len(arr)):
    if arr[i] == 0:
        j = i
        break
    
for i in range(j+1,len(arr)):
    if arr[i] != 0:
        arr[i],arr[j] = arr[j],arr[i]
        j+=1
    
print(arr)