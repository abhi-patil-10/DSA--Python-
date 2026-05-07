# Reverse the number
n = -123
sign = 1
if n < 0:
    sign = -1

reverse = 0
n = abs(n)
while n > 0:
    last_digit = n % 10
    n = n // 10
    reverse = reverse * 10 + last_digit
print(sign * reverse)