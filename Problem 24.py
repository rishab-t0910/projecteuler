def perm(x):
    a = str(x)
    return '0' in a and '1' in a and '2' in a and '3' in a and '4' in a and '5' in a and '6' in a and '7' in a and '8' in a and '9' in a
    
import time
start = time.process_time()

fact_two_count = 997920

for i in range(278134569, 278965431):
    if perm(i):
        fact_two_count += 1

    if fact_two_count == (10**6):
        print(i)
        break    

print(time.process_time() - start, 'sec')

#Mathematically deduced the first three digits to be 278
