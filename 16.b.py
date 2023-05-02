#! python3

def  odd(value: int) -> bool:
    """ Returns True if value odd, otherwise returns False
    """
    return bool(int(value) & 1)

a, b, c = map(odd, input().split())

print('WIN' if a == b == c else 'FAIL')
