def fact(n):
    k = 1
    for i in range(2,n+1):
        k *= i

    return k
        
    
import time
start = time.process_time()

total = 0

for i in range(3, 10000000):
    curr = str(i)
    comb = 0
    for a in curr:
        comb += fact(int(a))

    if(comb == i):
        total += i

print(total)
    

print(time.process_time() - start, 'sec')
