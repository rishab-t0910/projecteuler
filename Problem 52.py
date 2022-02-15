import math

def digits_in(x):
    a = str(x)
    fin = [0]*10

    for i in a:
        fin[int(i)] += 1

    return fin

        
import time
start = time.process_time()

for i in range(100000, 1000000):
    if digits_in(i) == digits_in(2*i) == digits_in(3*i) == digits_in(4*i) == digits_in(5*i) == digits_in(6*i):
        print(i, 2*i, 3*i, 4*i, 5*i, 6*i)


print(time.process_time() - start, 'sec')
