"""
*
**
***
****
*****
"""


for i in range(5):
    for j in range(i+1):
        print("*",end=" ")
    print()
    
    
    
"""
1
12
123
1234
12345
"""

for i in range(5):
    for j in range(i+1):
        print(j+1,end= " ")
    print()
    

"""
1
22
333
4444
55555
"""
for i in range(5):
    for j in range(i+1):
        print(i+1,end = " ")
    print()
    
"""
*****
****
***
**
*

"""
for i in range(5,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()
    


"""
12345
1234
123
12
1

"""

for i in range(5,0,-1):
    for j in range(i):
        print(j+1,end=" ")
    print()
    
    
"""
    *    
   ***   
  *****
 ******* 
*********

"""
n = 5
for i in range(n):
    # for spaces
    for j in range(n-i-1):
        print(" ",end=" ")
    
    #  for starts
    for j in range(2*i+1):
        print("*",end=" ")
    
    #for spaces
    for j in range(n-i-1):
        print(" ",end = " ")
    print()
    
""" 
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
"""

for i in range(n):
    #  for spaces
    for j in range(i):
        print(" ",end=" ")
        
    for j in range (2*n-2*i-1):
        print("*",end=" ")
        
    for j in range(i):
        print(" ",end=" ")
    print()
    


"""
*
**
***
****
*****
****
***
**
*

"""
n = 5
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()
for i in range(n-1,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()
    
    
start = 1
def pattern11(n):
    for i in range(n):
        if i%2 == 0:
            start = 1
        else:
            start = 0
            
        for j in range(i+1):
            print(start,end = " ")
            start = 1-start
        print()
        
def pattern12(n):
    space = 2*(n-1)
    for i in range(n):
        # numbers
        for j in range(i+1):
            print(j+1, end = " ")
        
        
        # space 
        for j in range(0,space):
            print(" ",end= " ")
        
        
        # numbers
        for j in range(i+1,0,-1):
            print(j,end = " ")
        space -= 2
        print()

def pattern13(n):
    num = 1
    for i in range(n):
        for j in range(i+1):
            print(num,end = " ")
            num += 1
            
        print()

def pattern14(n):
    x = 'A'
    for i in range(5):
        for j in range(i+1):
            print(chr(65+j),end = " ")
            
            
        print()

def pattern15(n):
    for i in range(n,0,-1):
        for j in range(i):
            print(chr(65+j),end = " ")
        print()

def pattern16(n):
    char = 65
    for i in range(n):
        for j in range(i+1):
            print(chr(char+i),end=" ")
            # char += 1
        print()

def pattern17(n):
    for i in range(n):
        char = 65
        breakpoint = (2*i+1)// 2
        # space
        for j in range(n-i-1):
            print(" ",end=" ")
            
        for j in range(2*i+1):
            print(chr(char),end=" ")
            if j < breakpoint:
                char += 1
            else:
                char -= 1
            
            
        for j in range(n-i-1):
            print(" ",end = " ")
        print()

def pattern18(n):
    for i in range(n):
        char = 65
        for j in range(i+1):
            print(chr(char+(n-i-1)),end= " ")
            char += 1
            
        print()

def pattern19(n):
    for i in range(n):
        # # starts
        for j in range(n-i):
            print("*",end=" ")
            
        # # space
        for j in range(2*i):
            print(" ",end=" ")
        
        # starts
        for j in range(n-i):
            print("*",end=" ")
            
        print()
    for i in range(n):
        # # starts
        for j in range(i+1):
            print("*",end=" ")
            
        # # space
        for j in range((2*n)-(2*(i+1))):
            print(" ",end=" ")
        
        # starts
        for j in range(i+1):
            print("*",end=" ")
            
        print()

def pattern20(n):
    for i in range(n):
        # stars
        for j in range(i+1):
            print("*",end=" ")
            
        # space
        for j in range((2*n)-(2*(i+1))):
            print(" ",end=" ")
        
        
        # stars
        for j in range(i+1):
            print("*",end=" ")
            
        print()
    for i in range(n):
        # stars
        for j in range(n-i):
            print("*",end=" ")
            
        # space
        for j in range(2*i):
            print(" ",end=" ")
        
        
        # # stars
        for j in range(n-i):
            print("*",end=" ")
            
        print()
    
def pattern21(n):
    for i in range(n):
        for j in range(n):
            if i==0 or i==n-1 or j==0 or j==n-1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()

pattern11(5)
pattern12(5)
pattern13(5)
pattern14(5)
pattern15(5)
pattern16(5)
pattern17(5)
pattern18(5)
pattern19(5)
pattern20(5)
pattern21(5)