def maxof(x, y, z):
    if x>=y and x>=z:
        return x

    elif y>=x and y>=z:
        return y

    else:
        return z
    
def up(array):
    fin = [0]*4
    maximum = -1

    for c in range(20):
        curr = 1
        for r in range(0, 16):
            curr = array[r][c] * array[r+1][c] * array[r+2][c] * array[r+3][c]

            if curr >= maximum:
                maximum = curr
                fin[0] = array[r][c]
                fin[1] = array[r+1][c]
                fin[2] = array[r+2][c]
                fin[3] = array[r+3][c]

                
    print('Up',fin, maximum)
    return maximum

def side(array):
    maximum = -1
    fin = [0]*4

    for r in range(20):
        curr = 1
        for c in range(0, 16):
            curr = array[r][c] * array[r][c+1] * array[r][c+2] * array[r][c+3]

            if curr >= maximum:
                maximum = curr
                fin[0] = array[r][c]
                fin[1] = array[r][c+1]
                fin[2] = array[r][c+2]
                fin[3] = array[r][c+3]

                
    print('Side', fin, maximum)
    return maximum

def diag(array):
    return 0

    
import time
start = time.process_time()

f = open('Problem 11.txt', 'r')
values = f.read()
values = values.split('\n')
new_values = []


for i in range(len(values)):
    row = []
    for a in range(0, len(values[i]), 3):
        curr = values[i][a]+values[i][a+1]
        row.append(int(curr))

    new_values.append(row)

print(maxof(up(new_values), side(new_values), diag(new_values)))


print(time.process_time() - start, 'sec')
