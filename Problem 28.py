import time
start = time.process_time()

res = [0]*9
res.append(537)

for i in range(10, 1002):
    if i % 2 == 0:
        res.append(0)
    else:
        res.append(res[i-2] + 4*(i**2) - 6*i + 6)

print(res[1001])

print(time.process_time() - start, 'sec')

#Mathematically determined a formula for the sum of the diagonals of an nxn spiral where n is odd
#P(n), where n is odd and the spiral is nxn
#P(n) = P(n-2) + 4n^2 - 6n + 6
