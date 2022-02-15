import time
start = time.process_time()

fin = []

for i in range(2, 1000000):
    tot = 0
    curr = str(i)
    for r in curr:
        tot += int(r)**5

    if tot == i:
        fin.append(i)

tot = 0

for i in fin:
    tot += i


print(tot)

print(time.process_time() - start, 'sec')
