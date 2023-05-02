#! python3

n = int(input())
s = list(map(int, input().split()))
a = [None] * n
p = []

l = None
for i in range(n):
    if s[i] == 0:
        a[i] = 0
        if l is None:
            a[0:i] = p[::-1]
        else:
            j = i - 1
            while (a[j] is None or a[j] > i - j) and j >= 0:
                a[j] = i - j
                j -= 1
        l = i
    elif l is None:
        p.append(len(p) + 1)
        continue
    else:
        a[i] = i - l

print(*a)
