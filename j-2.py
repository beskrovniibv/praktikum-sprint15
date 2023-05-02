n = int(input())
p = sorted(list(map(int, input().split())))
k = int(input())

l, r = 0, n -1
while p[l] + p[r] != k:
    if p[l] + p[r] > k:
        r = r - 1
    else:
        l = l + 1
    if l == r:
        break
r = f'{p[l]} {p[r]}' if l != r else 'None'
print(r)
