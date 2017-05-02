def array_left_rotation(a, n, k):
    index = k % n
    final_array = a[index:]
    final_array.extend(a[:index])
    return final_array 

n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print ' '.join(map(str,answer))
