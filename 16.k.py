#! python3

x = int(input())
l = list(map(int, input().split()))
k = input()
k = [int(c) for c in k]

i, j = len(l) - 1, len(k) - 1
p = 0
r = ''

while i >= 0 or j >= 0:
    li = l[i] if i >= 0 else 0
    kj = k[j] if j >= 0 else 0
    s = li + kj + p
    r = str(s % 10) + ' ' + r
    p = int(s >= 10)
    i -= 1
    j -= 1
if p:
    r = '1 ' + r
print(r)
