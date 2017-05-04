def calc_routes(n):
	start = [1, 2, 4]
	if n < 3:
		return start[n-1]
	for i in range(n-3):
		start.append(start[-1] + start[-2] + start[-3])
	return start[-1]


s = int(raw_input().strip())
for a0 in xrange(s):
    n = int(raw_input().strip())
    print calc_routes(n)
