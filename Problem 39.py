import math

def maxof(array):
    index = 1
    maximum = array[1]

    for i in range(1, len(array)):
        if array[i] > maximum:
            maximum = array[i]
            index = i

    print(maximum)
    return index
            
import time
start = time.process_time()

fin = [0]*1001
squares = []

for i in range(0, 1000):
    squares.append(i**2)

for a in range(2, 1001):
    for b in range(2, 1001):
        if a**2 + b**2 in squares:
            c = int(math.sqrt(a**2+b**2))

            if a+b+c <= 1000:
            
                fin[a+b+c] += 1
        
print(maxof(fin))

print(time.process_time() - start, 'sec')
