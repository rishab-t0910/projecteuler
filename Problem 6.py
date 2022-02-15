import time
start = time.process_time()

square = 0
norm_sum = 0

for i in range(101):
    square += (i**2)
    norm_sum += i

print((norm_sum**2) - square)
    
print(time.process_time() - start, 'sec')
