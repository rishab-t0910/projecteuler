import time
start = time.process_time()

fin = [1, 1]
c1 = 0
c2 = 1

while(len(str(fin[len(fin)-1])) < 1000):
    fin.append(fin[c1]+fin[c2])
    c1 += 1
    c2 += 1
    
print(fin[len(fin)-1])
print(len(fin))

print(time.process_time() - start, 'sec')
