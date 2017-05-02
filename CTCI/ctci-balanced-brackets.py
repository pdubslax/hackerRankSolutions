def is_matched(expression):
    stack = []
    for letter in expression:
        if letter == '{' or letter == '[' or letter == '(':
            stack.append(letter)
        if letter == '}' or letter == ']' or letter == ')':
            if len(stack) <= 0:
                return False
            check = stack.pop()
            if (check == '{' and letter != '}') or (check == '[' and letter != ']') or (check == '(' and letter != ')'):
                return False



    if len(stack) > 0:
        return False
    return True

test = "{{[[(()))]]}}"
print is_matched(test)

# t = int(raw_input().strip())
# for a0 in xrange(t):
#     expression = raw_input().strip()
#     if is_matched(expression) == True:
#         print "YES"
#     else:
#         print "NO"
