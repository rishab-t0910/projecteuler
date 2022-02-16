import math

import time
start = time.process_time()

pent = []
hect = []
mix = 143
last = 50000

for i in range(166, last):
    p = int((3*i*i - i)/2)
    pent.append(p)

    h = int(2*mix*mix - mix)
    mix += 1
    hect.append(h)

for i in pent:
    if i in hect:
        print(i)
        break

print(time.process_time() - start, 'sec')
