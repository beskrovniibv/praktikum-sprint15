#! python3

n = int(input())
s = [int(x) for x in  input().split()]
a = [None] * n

l = None
for i in range(n):
    if s[i] == 0:
        a[i] = 0
        j = i - 1
        while (a[j] is None or a[j] > i - j) and j >= 0:
            a[j] = i - j
            j -= 1
        l = i
    elif l is None:
        continue
    else:
        a[i] = i - l

print(*a)
