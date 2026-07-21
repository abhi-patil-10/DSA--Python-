arr = [1,1,1,1, 2, 2, 3, 3, 3, 4,5,5,5,5,5]

freq = {}
max = 0

for num in arr:
    if num in freq:
        freq[num] += 1
        if max < freq[num]:
            max = num
    else:
        freq[num] = 1
        
    
    

print(max)