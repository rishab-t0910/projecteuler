def properdiv(x):
    tot = 0
    for i in range(1, x):
        if x%i == 0:
            tot += i

    return tot
    
import time
start = time.process_time()

fin = [0]
#res = []
res = 0

for i in range(1, 10001):
    fin.append(properdiv(i))

for i in range(len(fin)):
    if fin[i]<len(fin):
        if i == fin[fin[i]] and fin[i]!=i:
            res += i
            
print(res)


print(time.process_time() - start, 'sec')
