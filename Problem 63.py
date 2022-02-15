def num_len(x):
    return len(str(x))

import time
start = time.process_time()

count = 0

for i in range(1, 300):
    for a in range(1, 1000):
        if num_len(a**i) == i:
            count += 1

print(count)
        

print(time.process_time() - start, 'sec')
