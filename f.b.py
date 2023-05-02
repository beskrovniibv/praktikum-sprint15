#! python3

# id 86762801


DIGITS = set('0123456789')


def read_values() -> tuple:
    max_keys_count = int(input())
    source = {}
    for _ in range(4):
        line = input()
        for char in line:
            if char not in DIGITS:
                continue
            source[char] = source.get(char, 0) + 1
    return (max_keys_count*2, source)


def solve(max_keys, source: dict) -> int:
    answear = 0
    for digit in source:
        if source[digit] <= max_keys:
            answear += 1
    return answear


if __name__ == '__main__':
    max_keys, source = read_values()
    result = solve(max_keys, source)
    print(result)
