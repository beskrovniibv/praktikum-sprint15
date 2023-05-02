#! python3

n = int(input())
v = list(map(int, input().split()))

r = 0
if n == 1:
    r = 1
else:
    if v[0] > v[1]:
        r += 1
    for i in range(1, n - 1):
        if v[i - 1] < v[i] and v[i] > v[i + 1]:
            r += 1
    if v[n - 1] > v[n - 2]:
        r += 1
print(r)
