def isArmstrong(n):
    original = n
    solution = 0

    while(n>0):
        last_digit = n%10
        solution = solution + last_digit*last_digit*last_digit
        n = n//10

    if solution == original:
        return True
    else:
        return False
    
num = int(input("Enter the number : "))
print(isArmstrong(num))