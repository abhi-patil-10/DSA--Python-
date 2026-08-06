#  7. Two Sum II – Input numsay Is Sorted:
#     Find two numbers whose sum equals the target
# varaity-1:
#     just return yes or no
# varaity-2:
#     return the index of element



# brute force
# def two_sum(nums,target):
#     for i in range(len(nums)):
#         for j in range(len(nums)):
#             if i != j:
#                 if nums[i]+nums[j] == target:
#                     return i,
#     return -1

# nums = [2,4,5,6,7]
# target = 11
# print(two_sum(nums,target))


# better approch for variaty 1 and 2 with littel modification
# def two_sum(nums,target):
#     hash = {}
#     for i in range(len(nums)):
#         moreNeeded = target - nums[i]
#         if moreNeeded not in hash:
#             hash[nums[i]] = i
#         else:
#             return {hash[moreNeeded],i}
#     return {-1,-1}

# nums = [2,4,5,6,7]
# target = 11
# print(two_sum(nums,target))

# optimal approch for variaty 1 (2-pointers)

def two_pointers(arr,target):
    # arr = sorted(arr)
    left = 0
    right = len(arr)-1
    while left < right:
        if arr[left]+arr[right] > target:
            right -= 1
        elif arr[left]+arr[right] < target:
            left += 1
        else:
            return True
    return False
    
arr = [4,1,2,3,1]
arr = sorted(arr)
print(two_pointers(arr,5))