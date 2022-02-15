import math

import time
start = time.process_time()

fin = '.'

for i in range(1, 185186):
    fin += str(i)

for i in range(7):
    print(10**i, ': ', fin[10**i])

print(time.process_time() - start, 'sec')
