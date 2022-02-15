import math

import time
start = time.process_time()

tri = []
pent = []

for n in range(286, 600):
    tri.append(int((n**2+n)/2))

for n in range(165, 600-286):
    pent.append(int(((3*n)**2-n)/2))

n = 144

while True:
    if (2*(n**2) - 1) in tri and (2*(n**2) - 1) in pent:
        print(2*(n**2) - 1)
        break

    n+=1

print(time.process_time() - start, 'sec')
