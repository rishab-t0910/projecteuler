import math
import time
start = time.process_time()

res = []

for a in range(2, 101):
    for b in range(2, 101):
        if (a**b) not in res:
            res.append(a**b)

print(len(res))

print(time.process_time() - start, 'sec')
