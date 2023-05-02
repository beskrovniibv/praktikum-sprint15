#! python3

n = int(input())
k = 2

while n != 1:
    if n % k == 0:
        n //= k
        print(k, end=' ')
    else:
        if k == 2:
            k += 1
        else:
            k += 2
        if  k*k > n:
            print(n)
            break
