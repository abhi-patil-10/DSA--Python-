# ar = list(map(int,input("Enter the numbers with space").split()))

# freq = {}

# for num in ar:
#     if num in freq:
#         freq[num] += 1
#     else:
#         freq[num] = 1
        

# q = int(input("Enter how many elements wants to check : "))

# for _ in range(q):
#     element = int(input("enter element : "))
#     print(freq.get(element,0))


# str = input("Enter string : ")

# freq = {}

# for s in str:
#     if s in freq:
#         freq[s] += 1
#     else:
#         freq[s] = 1

# q = int(input("how many chars you want to check :"))

# for _ in range(q):
#     element = int(input("Enter the element :"))
#     print(freq.get(element,0))
    
    
    
dictionary = {}
n = int(input("How many records you want to store : "))

for _ in range(n):
    name = input("Enter the name : ")
    age = int(input("Enter the age :"))
    dictionary[name] = age
    
  

print(dictionary)