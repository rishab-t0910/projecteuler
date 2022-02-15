def ispali(x):
    a = str(x)

    for i in range(len(a)):
        if a[i] != a[len(a)-1-i]:
            return False

    return True
    
import time
start = time.process_time()

maximum = 0

for i in range(999, 99, -1):
    for a in range(999, 99, -1):
        if ispali(i*a):
            if(i*a > maximum):
                maximum = i*a

print(maximum)
            

print(time.process_time() - start, 'sec')
