import time
start = time.process_time()

f = open('Problem 13.txt', 'r')
values = f.read()
new_val = values.split('\n')
print(new_val)

total = 0
for i in new_val:
    total += int(i)

print(total)

print(time.process_time() - start, 'sec')
