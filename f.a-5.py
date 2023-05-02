#! python3

def solve():
    n = int(input())
    s = input().split()  # [int(x) for x in input().split()]
    z = []
    for i in range(n):
        if s[i] == '0':
            z.append(i)

    l_prev = None
    l_next = 0
    ans = ''
    for i in range(n):
        if s[i] == '0':
            ans += '0 '
            l_prev = l_next
            if l_next + 1 < len(z):
                l_next += 1
            else:
                l_next = None
        else:
            if l_prev is None:
                ans += f'{z[l_next] - i} '
            elif l_next is None:
                ans += f'{i - z[l_prev]} '
            else:
                v1 = z[l_next] - i
                v2 = i - z[l_prev]
                if v1 < v2:
                    ans += f'{v1} '
                else:
                    ans += f'{v2} '
            pass

    print(ans)


if __name__ == '__main__':
    solve()
