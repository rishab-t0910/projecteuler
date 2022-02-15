def tiebreak(p1, p2, hand_val): #1 if p1 wins, 0 if p2 wins
    num_1 = [p1[0], p1[3], p1[6], p1[9], p1[12]]
    num = replacement(num_1)
    num_1.sort()
    
    num_2 = [p2[0], p2[3], p2[6], p2[9], p2[12]]
    num = replacement(num_2)
    num_2.sort()

    count_1 = [0]*15
    count_2 = [0]*15

    for i in range(0, 5):
        count_1[int(num_1[i])] += 1
        count_2[int(num_2[i])] += 1
        

    if hand_val == 1 or hand_val == 5 or hand_val == 6 or hand_val == 9: #high card, straight, flush, straight flush
        if(num_1[4] > num_2[4]):
            return 1
        else:
            return 0

    elif hand_val == 2: #one pair
        if count_1.index(2) > count_2.index(2):
            return 1
        else:
            return 0

    elif hand_val == 3: #two pair
        if count_1.index(2, count_1.index(2)) > count_2.index(2, count_2.index(2)):
            return 1
        else:
            return 0

    elif hand_val == 4 or hand_val == 7: #threes, full house
        if count_1.index(3) > count_2.index(3):
            return 1
        else:
            return 0

    elif hand_val == 8: #fours
        if count_1.index(4) > count_2.index(4):
            return 1
        else:
            return 0
        
    
def maxof(x, y):
    if x>y:
        return x
    return y
    
def isflush(suits):
    return suits[0] == suits[1] == suits[2] == suits[3] == suits[4]
    
def replacement(num):
    for i in range(len(num)):
        if num[i] == 'T':
            num[i] = 10

        elif num[i] == 'J':
            num[i] = 11

        elif num[i] == 'Q':
            num[i] = 12

        elif num[i] == 'K':
            num[i] = 13

        elif num[i] == 'A':
            num[i] = 14

        else:
            num[i] = int(num[i])

    return num
            
def hand(p1):
    maximum = 0
    highest = ''
    
    suits = [p1[1], p1[4], p1[7], p1[10], p1[13]]
    flush = isflush(suits)
    
    num = [p1[0], p1[3], p1[6], p1[9], p1[12]]
    
    num = replacement(num)

    num.sort()

    if num[0] == 10 and num[1] == 11 and num[2] == 12 and num[3] == 13 and num[4] == 14 and flush:
        maximum = 10 #Royal Flush

    if flush:
        count = 0

        if 14 in num:
            num.append(1)
            num.sort()
        
        for i in range(len(num)-1):
            if num[i+1] - num[i] == 1:
                count+= 1

        if count == 4:
            maximum = maxof(maximum, 9) #Straight flush

        else:
            maxmimum = maxof(maximum, 6) #flush

        highest = maxof(num[4], num[len(num)-1])

    else:
        vals = [0]*14
        two_count = 0
        
        for i in num:
            if i == 14:
                vals[1] += 1
            else:
                vals[i] += 1

        for i in vals:
            if i == 2:
                two_count += 1

        if 4 in vals:
            maximum = maxof(maximum, 8) #four of a kind
            highest = vals.index(4)

        elif 3 in vals and 2 in vals:
            maximum = maxof(maximum, 7) #full house
            highest = vals.index(3)

        elif 3 in vals and 2 not in vals:
            maximum = maxof(maximum, 4) #three of a kind
            highest = vals.index(3)

        if two_count == 2:
            maximum = maxof(maximum, 3) #two pairs
            highest = maxof(vals.index(2), vals.index(2, vals.index(2)))

        elif two_count == 1:
            maximum = maxof(maximum, 2) #one pair
            highest = vals.index(2)

        count = 0

        if 14 in num:
            num.append(1)
            num.sort()
        
        for i in range(len(num)-1):
            if num[i+1] - num[i] == 1:
                count+= 1

        if count == 4:
            maximum = maxof(maximum, 5) #Straight
            highest = maxof(num[4], num[len(num)-1])
            
    return maxof(maximum, 1)    
            
            
import time
start = time.process_time()
f = open('Problem 54.txt', 'r')
values = f.read()
new_values = values.split('\n')

p1_win = 0
p1 = []
p2 = []

for i in new_values:
    p1 = i[:14]
    p2 = i[15:]

    if hand(p1)>hand(p2):
        p1_win += 1
    
    elif hand(p1) == hand(p2):
        p1_win += tiebreak(p1, p2, hand(p1))

print(p1_win)

print(time.process_time() - start, 'sec')
