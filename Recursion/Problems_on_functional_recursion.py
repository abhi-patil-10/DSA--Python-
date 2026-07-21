#Q.1- Reverse the array using recursion

# def reverse(i,arr,n):
#     if i > (n//2):
#         print(arr)
#         return
    
#     arr[i],arr[n-i-1] = arr[n-i-1],arr[i]
    
#     reverse(i+1,arr,n)
    
# arr = list(map(int,input("Enter the numbers seperated by space").split()))
# n = len(arr)

# print(reverse(0,arr,n))

# Q.2 - Function to check if a string is a palindrome using recursion

def palindrome(i,str,n):
    if i > (n//2):
        return True
    if str[i] != str[n-i-1]:
        return False
    
    return palindrome(i+1,str,n)
    
str = "madam"
n = len(str)
print(palindrome(0,str,n))