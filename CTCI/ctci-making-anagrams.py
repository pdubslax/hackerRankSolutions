import collections as c

def number_needed(a,b):
    aDic = c.defaultdict(lambda: 0)
    bDic = c.defaultdict(lambda: 0)

    for letter in a:
        aDic[letter] += 1
    for letter in b:
        bDic[letter] += 1

    numSwaps = 0
    for key in aDic.keys():
        if aDic[key] > bDic[key]:
            numSwaps += aDic[key] - bDic[key]
            aDic[key] = bDic[key]
    for key in bDic.keys():
        if bDic[key] > aDic[key]:
            numSwaps += bDic[key] - aDic[key]
            bDic[key] = aDic[key]

    return numSwaps


a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)
