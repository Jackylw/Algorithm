# https://www.nowcoder.com/practice/aaf8b53f6ea74ad6beabed77bb275725
import sys
import bisect

M = dict()
M_list = []
M_len = 0


def insertValue(x):
    count = xCount(x)
    M[x] = count + 1
    if count == 0:
        bisect.insort(M_list, x)
    global M_len
    M_len += 1


def eraseValue(x):
    count = xCount(x)
    if count > 0:
        M[x] = count - 1
        global M_len
        M_len -= 1
        if count == 1:
            i = bisect.bisect_left(M_list, x)
            M_list.pop(i)


def xCount(x) -> int:
    return M.get(x, 0)


def sizeOfSet() -> int:
    return M_len


def getPre(x):
    i = bisect.bisect_left(M_list, x) - 1
    return -1 if i < 0 else M_list[i]


def getBack(x):
    i = bisect.bisect_right(M_list, x)
    return -1 if i >= len(M_list) else M_list[i]


def main():
    data = sys.stdin.read().split()
    data_iter = iter(data)

    n = int(next(data_iter))

    output = [""] * n
    output_ptr = -1

    for _ in range(n):
        command = next(data_iter)

        if command == "4":
            output_ptr += 1
            output[output_ptr] = f"{sizeOfSet()}"

        else:
            x = int(next(data_iter))

            if command == "1":
                insertValue(x)

            elif command == "2":
                eraseValue(x)

            elif command == "3":
                output_ptr += 1
                output[output_ptr] = f"{xCount(x)}"

            elif command == "5":
                output_ptr += 1
                output[output_ptr] = f"{getPre(x)}"

            elif command == "6":
                output_ptr += 1
                output[output_ptr] = f"{getBack(x)}"

    sys.stdout.write("\n".join(output[: output_ptr + 1]))


if __name__ == "__main__":
    main()
