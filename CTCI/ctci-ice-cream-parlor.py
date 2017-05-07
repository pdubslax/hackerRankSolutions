def findSum(money, costs):
	costList = sorted(costs)
	for i in range(len(costs)):
		startPrice = costs[i]
		target = money - startPrice
		low = 0
		high = len(costList)
		while(low < high):
			guess = ( high + low ) / 2
			
			if costList[guess] < target:
				low = guess + 1
			else:
				high = guess

			if costList[guess] == target:
				otherValue = costList[guess]
				for j,v in enumerate(costs):
					if v == otherValue:
						index2 = j
				print str(i+1) + " " + str(index2+1)
				return

def diffApp(flavors, M):
	flavor_map = {}
	for idx, flavor in enumerate(flavors):
		residual = (M - flavor)
		if residual in flavor_map:
			return sorted([flavor_map[residual], idx])
		if not flavor in flavor_map:
			flavor_map[flavor] = idx




t = int(raw_input().strip())
for a0 in xrange(t):
	m = int(raw_input().strip())
	n = int(raw_input().strip())
	a = map(int, raw_input().strip().split(' '))
	result_arr = diffApp(a, m)
	print result_arr[0]+1, result_arr[1]+1