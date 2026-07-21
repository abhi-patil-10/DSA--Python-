import numpy as np

m , n = map(int,input("Enter the number of rows and columns : ").split())
temp = []
for i in range(m):
    row = list(map(int,input("Enter row element :").split()))
    temp.append(row)
    
print(temp)