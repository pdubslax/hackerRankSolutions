def bubbleSort(numbers, values):
    totalSwaps = 0
    for i in range(numbers):
        newSwaps = 0
        for j in range(numbers-1):
            if values[j] > values[j+1]:
                values[j],values[j+1] = values[j+1],values[j]
                totalSwaps += 1
                newSwaps += 1
        if newSwaps == 0:
            break

    print "Array is sorted in " + str(totalSwaps) + " swaps."
    print "First Element: " + str(values[0])
    print "Last Element: " + str(values[-1])


n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))
bubbleSort(n,a)
