import math

def is_prime(num):
	if num == 2 or num == 3:
		return True
	if num == 1:
		return False
	for i in range(2,int(math.sqrt(num)+1)):
		if num % i == 0:
			return False
	return True



p = int(raw_input().strip())
for _ in xrange(p):
    n = int(raw_input().strip())
    if is_prime(n):
    	print "Prime"
    else:
    	print "Not prime"
