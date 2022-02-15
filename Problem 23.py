def properdiv(x):
    tot = 0
    for i in range(1, x):
        if x%i == 0:
            tot += i

    if tot>x:
        return 1 #abundant
    else:
        return 2 #fuck knows
    
import time
start = time.process_time()

s = 28124
mega = []
res = [0]*s
tot = 0

for i in range(0, s):
    if properdiv(i) == 1:
        mega.append(i)

for x in range(0, len(mega)):
    for y in range(x, len(mega)):
        curr = mega[x]+mega[y]

        if curr<s:
            if res[curr] == 0:
                res[curr] = curr

for i in range(len(res)):
    if res[i] == 0:
        tot += i

print(tot)

print(time.process_time() - start, 'sec')
