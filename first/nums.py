import random
N = 10
arr = [0] * N
for i in range (N):
    arr[i] = random.randint(1, 100)

def average(arr):
    s = 0
    for i in range (N):
        s = 0
        for i in range(N):
            s += arr[i]
        return s/N
print(arr)
print(average(arr))











