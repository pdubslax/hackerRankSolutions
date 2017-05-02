import collections as c

def ransom_note(magazine, ransom):
    wordBank = c.defaultdict(lambda: 0)

    for word in magazine:
        wordBank[word] += 1

    for word in ransom:
        if wordBank[word] <= 0:
            return False
        else:
            wordBank[word] -= 1
    return True

m, n = map(int, raw_input().strip().split(' '))
magazine = raw_input().strip().split(' ')
ransom = raw_input().strip().split(' ')

# magazine = ['give', 'me', 'one', 'grand', 'today', 'night']
# ransom = ['give', 'one', 'grand', 'today', 'yo']
answer = ransom_note(magazine, ransom)
if(answer):
    print "Yes"
else:
    print "No"
