import numpy

N = int(input())
A = numpy.array([list(map(float,input().split()))])
ans = numpy.linalg.det(A)
print(round(ans,2))
# print(ans)