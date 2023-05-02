#! python3

# id 86761667

def solve(source: list) -> list:
    length = len(source)
    answear = [None] * length
    lelf = None
    for index in range(length):
        if source[index] == 0:
            answear[index] = 0
            step_rigth_index = index - 1
            while ((answear[step_rigth_index] is None or
                    answear[step_rigth_index] > index - step_rigth_index) and
                   step_rigth_index >= 0):
                answear[step_rigth_index] = index - step_rigth_index
                step_rigth_index -= 1
            lelf = index
        elif lelf is None:
            continue
        else:
            answear[index] = index - lelf

    return answear


def read_values() -> list:
    int(input())
    source = [int(x) for x in input().split()]
    return source


def print_result(value: list):
    print(*value)


if __name__ == '__main__':
    source = read_values()
    result = solve(source)
    print_result(result)
