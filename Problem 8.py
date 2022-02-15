import time
start = time.process_time()

f = open('Problem 8.txt', 'r')
values = f.read()
new_values = values.replace('\n', '')

maximum = 0

for i in range(len(new_values)-13):
    curr = 1
    for a in range(i, i+13):
        curr *= int(new_values[a])

    if curr>maximum:
        maximum = curr

print(maximum)
        

print(time.process_time() - start, 'sec')
