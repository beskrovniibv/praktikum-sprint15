#! python3

s1 = sorted(input())
s2 = sorted(input())

for i in range(len(s1)):
    if s1[i] != s2[i]:
        print(s2[i])
else:
    print(s2[len(s2) - 1])

