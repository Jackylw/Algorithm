import heapq
import math
import sys

input = sys.stdin.readline


def f():
    n, w = map(int, input().split())
    rulers = []
    for _ in range(n):
        x, y = map(int, input().split())
        rulers.append((x, y))

    # 每个尺子的当前打磨量
    t = [0] * n
    # 当前斜边
    current_hypotenuse = [math.sqrt(x * x + y * y) for x, y in rulers]

    # 最大堆：存储 (-delta, i)，delta 是打磨1单位带来的斜边减少量
    heap = []
    for i in range(n):
        if t[i] < rulers[i][1]:
            # 计算打磨1单位的收益
            delta = current_hypotenuse[i] - math.sqrt(rulers[i][0] * rulers[i][0] + (rulers[i][1] - t[i] - 1) ** 2)
            heapq.heappush(heap, (-delta, i))

    total_t = 0
    total_sum = sum(current_hypotenuse)

    # 模拟 w 次打磨
    while heap and total_t < w:
        neg_delta, i = heapq.heappop(heap)
        delta = -neg_delta

        # 如果已经打磨到极限，跳过
        if t[i] >= rulers[i][1]:
            continue

        # 执行打磨
        t[i] += 1
        total_t += 1
        current_hypotenuse[i] = math.sqrt(rulers[i][0] * rulers[i][0] + (rulers[i][1] - t[i]) ** 2)

        # 更新该尺子的下一次收益
        if t[i] < rulers[i][1]:
            next_delta = current_hypotenuse[i] - math.sqrt(rulers[i][0] * rulers[i][0] + (rulers[i][1] - t[i] - 1) ** 2)
            heapq.heappush(heap, (-next_delta, i))

        total_sum -= delta

    print(f"{total_sum:.10f}")


if __name__ == '__main__':
    f()
