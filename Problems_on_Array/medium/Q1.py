#  7. Two Sum II – Input Array Is Sorted:
#     Find two numbers whose sum equals the target



# brute force
# def two_sum(arr,target):
#     for i in range(len(arr)):
#         for j in range(len(arr)):
#             if i != j:
#                 if arr[i]+arr[j] == target:
#                     return i,
#     return -1

# arr = [2,4,5,6,7]
# target = 11
# print(two_sum(arr,target))


# better approch
def two_sum(arr,target):
    hash = {}
    for i in range(len(arr)):
        more = target - arr[i]
        if more not in hash:
            hash[arr[i]] = i
        else:
            return {hash[more],i}
    return {-1,-1}

arr = [2,4,5,6,7]
target = 11
print(two_sum(arr,target))