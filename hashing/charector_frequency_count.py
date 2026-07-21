# this frequecy count valid to only a-z that is asci 97-122 not all 255 ascii's
# s = input("Enter the string :")

# hash_arr = [0] * 26

# for c in s:
#     hash_arr[ord(c) - ord('a')] += 1

# q = int(input("Enter how many char you want to check :"))

# while q > 0:
#     charector = input("Enter char to check :")
#     print(hash_arr[ord(charector) - ord('a')])
#     q -= 1



# for all ascii which include all the values 0-255 ascii

s = input("Enter the string :")

hash_arr = [0] * 255

for c in s:
    hash_arr[ord(c)] += 1


q = int(input("Enter how many char you want to check :"))

while q > 0:
    charector = input("Enter char to check :")
    print(hash_arr[ord(charector)])
    q -= 1