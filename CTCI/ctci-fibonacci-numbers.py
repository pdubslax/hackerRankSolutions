def fibonacci(n):
    # Write your code here.
    start = [0, 1]
    for i in range(n-1):
    	start.append(start[-1] + start[-2])
    return start[-1]

n = int(raw_input())
print(fibonacci(n))
