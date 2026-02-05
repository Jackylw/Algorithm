import sys
import bisect

M = set()
M_list = []


def insertValue(x):
    if x not in M:
        M.add(x)
        bisect.insort(M_list, x)


def eraseValue(x):
    if x in M:
        M.remove(x)
        i = bisect.bisect_left(M_list, x)
        M_list.pop(i)


def xInSet(x) -> bool:
    return x in M


def sizeOfSet() -> int:
    return len(M)


def getPre(x):
    i = bisect.bisect_left(M_list, x) - 1
    return -1 if i < 0 else M_list[i]


def getBack(x):
    i = bisect.bisect_right(M_list, x)
    return -1 if i >= sizeOfSet() else M_list[i]


def main():
    data = sys.stdin.read().split()
    data_iter = iter(data)

    n = int(next(data_iter))

    output = [''] * n
    output_ptr = -1

    for _ in range(n):
        command = next(data_iter)

        if command == '4':
            output_ptr += 1
            output[output_ptr] = f'{sizeOfSet()}'

        else:
            x = int(next(data_iter))

            if command == '1':
                insertValue(x)

            elif command == '2':
                eraseValue(x)

            elif command == '3':
                output_ptr += 1
                output[output_ptr] = ("YES" if xInSet(x) else "NO")

            elif command == '5':
                output_ptr += 1
                output[output_ptr] = f'{getPre(x)}'

            elif command == '6':
                output_ptr += 1
                output[output_ptr] = f'{getBack(x)}'

    sys.stdout.write('\n'.join(output[: output_ptr + 1]))


if __name__ == "__main__":
    main()
