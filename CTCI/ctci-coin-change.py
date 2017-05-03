import sys

def change_help(coins, num_coins, target):
    # if target == 0:
    #     return 1
    # if target < 0:
    #     return 0
    # if num_coins  <= 0 and target >= 1:
    #     return 0
    # return change_help(coins, num_coins - 1, target) + change_help(coins, num_coins, target - coins[num_coins -1])

    table = [[0 for x in range(num_coins)] for y in range(target + 1)]
    for i in range(num_coins):
        table[0][i] = 1

    for j in range(1,target+1):
        for k in range(num_coins):
            if j - coins[k] >= 0:
                x = table[j - coins[k]][k]
            else:
                x = 0

            if k >= 1:
                y = table[j][k-1]
            else:
                y = 0

            table[j][k] = x + y
    return table[target][num_coins - 1]



def make_change(coins, n):
    return change_help(coins, len(coins), n)

# n,m = raw_input().strip().split(' ')
# n,m = [int(n),int(m)]
# coins = map(int,raw_input().strip().split(' '))

coins = [1,2,3]
n = 4
print make_change(coins, n)
