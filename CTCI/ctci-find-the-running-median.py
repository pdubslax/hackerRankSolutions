import sys

def insert(array, val):

    low = 0
    high = len(array)
    guess = ( low + high ) / 2
    while low < high:
        if val > array[guess]:
            low = guess + 1
        else:
            high = guess
        guess = ( low + high ) / 2

    array.insert(guess,val)

    return array


def find_median(array):
    size = len(array)
    if size % 2 ==0:
        #average
        return ( array[size/2] + array[size/2 - 1] ) / 2.0
    else:
        return array[size/2]


n = int(raw_input().strip())
a = []
a_i = 0


for a_i in xrange(n):
    a_t = int(raw_input().strip())
    a = insert(a,a_t)
    print "%.1f" % find_median(a)
