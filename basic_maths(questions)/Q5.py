# Given two integers N1 and N2, find their greatest common divisor.

def gcd(n1,n2):
    
    gcd = 0
    for i in range(1 , min(n1,n2)+1):
        if n1%i==0 and n2%i==0:
            gcd = i
    return gcd

print(gcd(20,15))