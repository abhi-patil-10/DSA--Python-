# Check if a number is Palindrome or Not
n = 1312
original = n
reverse = 0


while(n > 0):
    last_digit = n%10
    n = n//10
    reverse = reverse*10 + last_digit

if reverse == original:
    print("Palindrome")
else:   print("Not Palindrome")