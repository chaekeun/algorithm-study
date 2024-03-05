import math

array = [True for i in range(n+1)]

for i in range(2, int(math.sqrt(n))+1):
    if array[i] == True:
        j = 2
        while i*j<=n:
            arra[i*j] = False
            j+=1

            