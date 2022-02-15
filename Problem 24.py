def perm(x):
    a = str(x)
    return '0' in a and '1' in a and '2' in a and '3' in a and '4' in a and '5' in a and '6' in a and '7' in a and '8' in a and '9' in a
    
import time
start = time.process_time()

fact_two_count = 999996

for i in range(2783915046, 2783915640):
    if perm(i):
        fact_two_count += 1

    if fact_two_count == (10**6):
        print(i)
        break    

print(time.process_time() - start, 'sec')

#Mathematically deduced the first seven digits to be 2783915
