# Print all Divisors of a given Number

def find_divisors(n):
    div_list = []

    for i in range(1,n+1):
        if n%i == 0:
            div_list.append(i)

    return div_list

print(find_divisors(12))