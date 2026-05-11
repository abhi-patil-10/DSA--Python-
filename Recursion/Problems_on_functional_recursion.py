#Q.1- Reverse the array using recursion

# def f(i,arr,n):
#     if i >= (n/2):
#         return
    
#     arr[i] , arr[n-i-1] = arr[n-i-1],arr[i]
#     f(i+1,arr,n)


# n = int(input("Enter the size of your array : "))
# arr = []
# for i in range(n):
#     num= int(input(f"Enter the {i+1} element"))
#     arr.append(num)
    
# f(0,arr,n)
# print(arr)



# Q.2 - Function to check if a string is a palindrome using recursion

def palindrom(i,str):
    if i >= len(str)//2:
        return True
    
    if str[i] != str[len(str)-i-1]:
        return False
    
    return palindrom(i+1,str)
    
    
str="madam"
print(palindrom(0,str))