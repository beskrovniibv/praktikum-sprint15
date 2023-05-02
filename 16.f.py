#! python3

s = input()

result = True
l = 0
r = len(s) - 1
while l < r:
    while not s[l].lower() in 'abcdefghijklmopqrstuvwxyz':
        l += 1
    while not s[r].lower() in 'abcdefghijklmopqrstuvwxyz':
        r -= 1
    if s[l].lower() != s[r].lower():
        result = False
        break
    l += 1
    r -= 1

print(result)
