arr = list(map(int,input("Enter numbers with space seperated :").split()))

# initial hash array with zeros
hash_arr = [0] * 10

# pre-computation
for num in arr:
    hash_arr[num] += 1

# print(hash_arr)
q = int(input("enter how many elements to check :"))

# fetch
while q > 0:
    number = int(input("enter checking element : "))
    print(hash_arr[number])
    q -= 1

