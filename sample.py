import numpy

arr = [1 ,2, 6, 5, 4, 4, 2, 5, 3, 6, 1, 6, 5, 3, 2, 4, 1, 2, 5, 1, 4, 3, 6, 8, 4, 3, 1, 5, 6, 2]

freq = {}
low = 0
for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        low = num
        freq[num] = 1
        
print(freq)
print(low)