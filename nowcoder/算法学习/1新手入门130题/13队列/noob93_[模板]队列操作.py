# https://www.nowcoder.com/practice/1137c8f6ffac4d5d94cc1b0cb08723f9
from collections import deque
t = int(input())
queue = deque()
for i in range(t):
    opt = list(map(int, input().split()))
    if opt[0] == 1:
        queue.append(opt[1])
    elif opt[0] == 2:
        if queue:
            queue.popleft()
        else:
            print('ERR_CANNOT_POP')
    elif opt[0] == 3:
        if queue:
            print(queue[0])
        else:
            print('ERR_CANNOT_QUERY')
    elif opt[0] == 4:
        print(len(queue))
