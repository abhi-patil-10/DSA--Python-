########## TWO POINTERS #########


# reverse an array element
# arr = [1,2,3,4,5]
# i = 0
# j = len(arr)-1

# while i<j:
#     if i != j:
#         arr[i],arr[j] = arr[j],arr[i]
#         i+=1
#         j-=1
#     else:
#         break

# print(arr)

# check the string is palindrome or not (in true or false)
# def pali(string):
    
#     i = 0
#     j = len(string)-1

#     while i<j:
        
#         if string[i] == string[j]:
#             i+=1
#             j-=1
#         else:
#             return False
    
#     return True
            


# string = "nmadam"
# print(pali(string))


# Valid Palindrome (Ignore spaces and special characters)
# string = "A man, a plan, a canal: Panama" 

# def valid_pali(string):
#     temp = []
    
#     for i in range(len(string)):
#         if string[i].isalpha():
#             temp.append(string[i].lower())
#     i=0
#     j = len(temp)-1
#     while i<j:
        
            
#         if temp[i] == temp[j]:
#             i+=1
#             j-=1
#         else:
#             return False
        
#     return True


# print(valid_pali(string))


#move all the zeros at the end

# arr = [1,2,0,3,0,4,0,0,5]
# j=0
# for i in range(len(arr)):
#     if arr[i] ==0:
#         j = i
#         break

# for i in range(j+1,len(arr)):
#     if arr[i] != 0:
#         arr[j],arr[i] = arr[i],arr[j]
#         j += 1

# print(arr)

# remove duplicate from sorted array
arr = [1,1,2,3,3,3,4]
i=0
for j in range(i+1,len(arr)):
    if arr[j] != arr[i]:
        arr[i+1] = arr[j]
        i+=1
print(arr[:i+1])