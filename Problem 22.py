import time
start = time.process_time()
f = open('Problem 22.txt', 'r')
values = f.read()
new_val = values.split(',')
new_val = [i.replace('"', '') for i in new_val] 
new_val.sort()

alp = "0ABCDEFGHIJKLMNOPQRSTUVWXYZ"

total = 0

for i in range(len(new_val)):
    curr = 0
    for r in new_val[i]:
        curr += alp.index(r)

    total += (curr*(i+1))

print(total)

print(time.process_time() - start, 'sec')
