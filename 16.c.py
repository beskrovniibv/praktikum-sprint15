#! python3

n = int(input())
m = int(input())
v = [list(map(int, input().split())) for _ in range(n)]
r = int(input())
c = int(input())

s = []

if r > 0:
    s.append(v[r - 1][c])
if r < n - 1:
    s.append(v[r + 1][c])
if c > 0:
    s.append(v[r][c - 1])
if c < m - 1:
    s.append(v[r][c + 1])
print(*sorted(s))
