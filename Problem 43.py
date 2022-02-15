import math

def pandigital(i):
    a = str(i)
    return '0' in a and '1' in a and '2' in a and '3' in a and '4' in a and '5' in a and '6' in a and '7' in a and '8' in a and '9' in a

def div_check(i):
    a = str(i)
    div_2 = int(a[1]+a[2]+a[3]) % 2 == 0
    div_3 = int(a[2]+a[3]+a[4]) % 3 == 0
    div_5 = int(a[3]+a[4]+a[5]) % 5 == 0
    div_7 = int(a[4]+a[5]+a[6]) % 7 == 0
    div_first = int(a[5]+a[6]+a[7]) % 11 == 0
    div_sec = int(a[6]+a[7]+a[8]) % 13 == 0
    div_last = int(a[7]+a[8]+a[9]) % 17 == 0

    return div_last and div_sec and div_first and div_7 and div_5 and div_3 and div_2

import time
start = time.process_time()

total = 0

for i in range(1023456789, 9876543210):
    if pandigital(i):
        if div_check(i):
            print(i)
            total += i

print(time.process_time() - start, 'sec')
