import time
start = time.process_time()

f1 = 1
f2 = 2
f3 = 3

total = 2

while f3 <= 4*(10**6):
    f3 = f1 + f2
    f1 = f2
    f2 = f3

    if f3%2 == 0:
        total += f3

print(total)
    

print(time.process_time() - start, 'sec')
