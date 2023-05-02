#! python

def solve():
    n = int(input())
    source = input().split()
    ans = ''
    zero_index, index = 0, 0
    z_l, z_r = None, None
    while zero_index < n:
        while source[zero_index] != '0':
            zero_index += 1
            if zero_index == n:
                break
        if z_r is not None:
            z_l = z_r
        if zero_index == n:
            z_r = None
        else:
            z_r = zero_index
        index = z_l + 1 if z_l is not None else 0
        while index < zero_index:
            if z_l is None:
                ans += f'{z_r - index} '
            elif z_r is None:
                ans += f'{index - z_l} '
            else:
                v1 = z_r - index
                v2 = index - z_l
                if v1 < v2:
                    ans += f'{v1} '
                else:
                    ans += f'{v2} '
            index += 1
        if z_r is not None:
            ans += '0 '
        zero_index += 1
    print(ans)


if __name__ == '__main__':
    solve()
