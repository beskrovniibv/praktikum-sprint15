#! python3

n = int(input())

r = ''
while n > 0:
    b = n & 1
    n //= 2
    r = str(b) + r

print(r) if r else print(0)
