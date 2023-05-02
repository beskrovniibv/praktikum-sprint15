#! python3

n = int(input())

if n == 1:
    print(True)
else:
    while n > 1:
        r = n % 4
        n //= 4
        if r != 0:
            print(False)
            break
    else:
        print(True)
