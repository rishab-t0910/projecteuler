import math

def isprime(x):

    if x<0:
        x = x*-1
    
    for i in range(2, int(math.sqrt(x))+1):
        if x%i == 0:
            return False

    return True

import time
start = time.process_time()

maximum = 0
coeff_1 = 0
coeff_2 = 0
primes = []

for i in range(1, 1001):
    if isprime(i):
        primes.append(i)
        primes.append(-i)

primes.sort()

for a in range(len(primes)):
    for b in range(len(primes)):
        n = 0
        count = 0 
        while (isprime(n**2 + primes[a]*n + primes[b])):
            count += 1
            n +=1
        
        if count >= maximum:
            maximum = count
            coeff_1 = primes[a]
            coeff_2 = primes[b]
            count = 0
            
print(coeff_1, coeff_2, maximum)   

##n = 0
##while isprime(n**2 + coeff_1*n+coeff_2):
##    print(n**2 + coeff_1*n+coeff_2, isprime(n**2 + coeff_1*n+coeff_2))
##    n += 1
##
##print(n)

print(time.process_time() - start, 'sec')
