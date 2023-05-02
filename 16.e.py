#! python3

n = int(input())

w = input().split()

l = 0
www = ''
for ww in w:
    ll = len(ww)
    if ll > l:
        l = ll
        www = ww

print(www)
print(len(www))
