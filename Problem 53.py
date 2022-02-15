import math

def fact(x):
    a = 1
    for i in range(2, x+1):
        a *= i

    return a

import time
start = time.process_time()

count = 0

for n in range(23, 101):
    num = fact(n)
    for a in range(0, n+1):
        d1 = fact(n-a)
        d2 = fact(a)
        d3 = d1*d2

        if num/d3 > (10**6):
            count+=1

print(count)

        
print(time.process_time() - start, 'sec')
