# Find the unique element in an array where every element is repeated twice except for one element.

#brute force
# nums = [4,1,2,1,2]
# counter = 0
# for i in range(len(nums)):
#     for j in range(len(nums)):
#         if nums[i] == nums[j]:
#             counter += 1

#     if counter == 1:
#         print(nums[i])



# using hashing(array):
# this solution feilds for negative numbers and 0 as well and some test cases also like [2,2,1]
# arr = [1]
# maxi = 0
# for i in range(len(arr)):
#     maxi = max(maxi,arr[i])
# hash_array = [0] * maxi

# for i in arr:
#     hash_array[i] += 1

# for i in range(len(hash_array)):
#     if hash_array[i] == 1:
#         print(i)


# using hashing (dictionary)
# arr = [1,1,2,2,3,3,4,5,5]
# freq = {}

# for i in arr:
#     if i in freq:
#         freq[i] += 1
#     else:
#         freq[i] = 1
    
# for i in range(1,len(freq)+1):
#     if freq[i] == 1:
#         print(i )



# optimal solution using xor 
arr = [4,1,2,1,2]
ans = 0
for i in range(len(arr)):
    ans = ans ^ arr[i]
    
print(ans)