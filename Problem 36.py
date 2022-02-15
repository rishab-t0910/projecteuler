import math
def is_pali(x):
    a = str(x)

    for i in range(len(a)):
        if a[i] != a[len(a)-1-i]:
            return False

    return True

import time
start = time.process_time()

total = 0

for i in range(10**6):
    if is_pali(i) and is_pali(bin(i)[2:]):
        total += i

print(total)

print(time.process_time() - start, 'sec')
