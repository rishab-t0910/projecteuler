import time
start = time.process_time()

n = 1

for i in range(2,101):
    n*=i

n = str(n)
total = 0

for i in range(len(n)):
    total += int(n[i])

print(total)
    

print(time.process_time() - start, 'sec')
