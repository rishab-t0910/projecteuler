import time
start = time.process_time()
f = open('Problem 42.txt', 'r')
values = f.read()
new_val = values.split(',')
new_val = [i.replace('"', '') for i in new_val] 

triangle = [0]*365
count = 0
alp = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in range(365):
    triangle[i] = int(i*(i+1)/2)

for i in new_val:
    total = 0
    for r in i:
        total += alp.index(r)

    if total in triangle:
        count += 1

print(count)

print(time.process_time() - start, 'sec')
