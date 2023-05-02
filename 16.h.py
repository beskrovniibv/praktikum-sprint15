#! python3

a = input()
b = input()

i = len(a) - 1
j = len(b) - 1

result = ''
p = '0'

while i >= 0 or  j >= 0:
    ai = a[i] if i >= 0 else '0'
    bj = b[j] if j >= 0 else '0'
    if ai == '1' and bj == '1' and p == '0':
        result = '0' + result
        p = '1'
    elif ai == '1' and bj == '1' and p == '1':
        result = '1' + result
        p = '1'
    elif (ai == '1' or bj == '1') and p == '1':
        result = '0' + result
        p = '1'
    elif (ai == '1' or bj == '1') and p == '0':
        result = '1' + result
    elif p == '1':
        result = '1' + result
        p = '0'
    else:
        result = '0' + result
    i -= 1
    j -= 1

if p == '1':
    result = '1' + result
    
print(result)
