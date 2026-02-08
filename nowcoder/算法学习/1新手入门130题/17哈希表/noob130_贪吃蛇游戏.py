# https://www.nowcoder.com/practice/ec61c899432f469bb8b3f96b44c23e79
import sys
from collections import deque

input = sys.stdin.readline

def moveSnake(dir):
    """
    位移逻辑，尾巴移除，头部添加
    """
    x, y = snake[-1]  # 头
    new_head = None
    if dir == 1:
        new_head = (x, y + 1)
    elif dir == 2:
        new_head = (x, y - 1)
    elif dir == 3:
        new_head = (x - 1, y)
    elif dir == 4:
        new_head = (x + 1, y)
    remove_tail = snake.popleft()
    snake_set.remove(remove_tail)
    if new_head in snake_set:
        # 保留事故现场前的最后一幕
        snake.appendleft(remove_tail)
        snake_set.add(remove_tail)
        return False
    snake.append(new_head)
    snake_set.add(new_head)
    return True


def eatSnake(dir):
    """
    吃蛇逻辑，头部添加，尾巴不移除
    """
    x, y = snake[-1]  # 头
    new_head = None
    if dir == 1:
        new_head = (x, y + 1)
    elif dir == 2:
        new_head = (x, y - 1)
    elif dir == 3:
        new_head = (x - 1, y)
    elif dir == 4:
        new_head = (x + 1, y)
    if new_head in snake_set:
        return False
    snake.append(new_head)
    snake_set.add(new_head)
    return True


# pop 出来是队头
snake = deque()
snake_set = set()  # 专门优化查询的，不然超时
n, q = map(int, input().split())
for _ in range(n):
    x, y = map(int, input().split())
    snake.append((x, y))
    snake_set.add((x, y))
for _ in range(q):
    parts = input().split()
    op_type = int(parts[0])
    direction = int(parts[1])

    success = False
    if op_type == 1:
        success = moveSnake(direction)
    elif op_type == 2:
        success = eatSnake(direction)

    if success:
        out_buffer = [f"{pos[0]} {pos[1]}" for pos in reversed(snake)]
        sys.stdout.write('\n'.join(out_buffer) + '\n') # 优化
    else:
        print("-1")
        exit()
