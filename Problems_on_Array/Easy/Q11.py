#maximum consecutive 1's in an array


arr = [1,1,0,1,1,1,0,1,1,1,1]
max_counter = 0    

counter = 0
for i in range(len(arr)):
    if arr[i] == 1 :
        counter += 1
        if counter > max_counter:
            max_counter = counter
    else:
        counter = 0





print(max_counter)
        
        
        