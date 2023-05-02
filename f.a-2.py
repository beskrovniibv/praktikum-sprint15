#! python3

n = int(input())
s = [int(x) for x in input().split()]
a = [0] * n
z = []

for i in range(n):
    if s[i] == 0:
        z.append(i)

z1 = 0
z2 = None
for i in range(n):
    if s[i] == 0:
        if z1 < len(z) - 1:
            z2 = z1
            z1 += 1
        continue
    if z2 is None:
        l = abs(z[z1] - i)
    else:
        l = min(abs(z[z1] - i), abs(z[z2] - i))
    a[i] = l

print(*a)
