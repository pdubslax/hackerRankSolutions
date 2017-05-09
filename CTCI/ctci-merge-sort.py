def merge(left, middle, right):
	global original
	global temp

	i = left
	j = middle
	k = left
	inv_count = 0

	while i <= middle -1 and j <= right:
		if original[i] <= original[j]:
			temp[k] = original[i]
			k += 1
			i += 1
		else:
			temp[k] = original[j]
			k += 1
			j += 1

			inv_count += middle - i

	while i <= middle - 1:
		temp[k] = original[i]
		k += 1
		i += 1

	while j <= right:
		temp[k] = original[j]
		k += 1
		j += 1

	for z in range(left, right + 1):
		original[z] = temp[z]

	return inv_count


def mergeSort(left, right):
	global original
	global temp

	mid = 0
	inv_count = 0

	if right > left:
		mid = (left + right)/2

		inv_count += mergeSort(left, mid)
		inv_count += mergeSort(mid + 1, right)

		inv_count += merge(left, mid + 1, right)

	return inv_count


original = [2, 1, 3, 1, 2]
temp = [0 for i in range(len(original))]
print mergeSort(0, len(original) - 1)


# t = int(raw_input().strip())
# for a0 in xrange(t):
#     n = int(raw_input().strip())
#     arr = map(int, raw_input().strip().split(' '))
#     original = list(arr)
#     temp = [0 for i in range(len(original))]
#     print mergeSort(0, len(original) - 1)
#     # print original