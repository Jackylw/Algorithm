# https://www.nowcoder.com/practice/ed27560740114f07a23fad98afac12b6
class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


n, m = map(int, input().split())
queue = input().split()

# 使用字典存储每个值对应的节点
node_map = {}

# 构建双向链表
head = ListNode(queue[0])
node_map[queue[0]] = head
current = head

for i in range(1, n):
    new_node = ListNode(queue[i])
    node_map[queue[i]] = new_node
    current.next = new_node
    new_node.prev = current
    current = new_node

# 处理插队操作
for _ in range(m):
    x, y = input().split()
    node_x = node_map[x]
    node_y = node_map[y]

    # 如果 x 已经在 y 前面，跳过
    if node_x.next == node_y:
        continue

    # 1. 将 x 从原位置移除
    if node_x.prev:
        node_x.prev.next = node_x.next
    else:
        # x 是头节点
        head = node_x.next

    if node_x.next:
        node_x.next.prev = node_x.prev

    # 2. 将 x 插入到 y 前面
    node_x.next = node_y
    node_x.prev = node_y.prev

    if node_y.prev:
        node_y.prev.next = node_x
    else:
        # y 是头节点，x 成为新头
        head = node_x

    node_y.prev = node_x

# 输出结果
result = []
current = head
while current:
    result.append(current.val)
    current = current.next

print(' '.join(result))


