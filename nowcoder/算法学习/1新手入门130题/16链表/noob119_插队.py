# https://www.nowcoder.com/practice/ed27560740114f07a23fad98afac12b6
class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


n, m = map(int, input().split())
queue = input().split()
node_map = {}
head = ListNode(queue[0])
node_map[queue[0]] = head
current = head

for i in range(1, n):
    new_node = ListNode(queue[i])
    node_map[queue[i]] = new_node
    current.next = new_node
    new_node.prev = current
    current = new_node

for _ in range(m):
    x, y = input().split()
    node_x = node_map[x]
    node_y = node_map[y]
    if node_x.next == node_y:
        continue
    if node_x.prev:
        node_x.prev.next = node_x.next
    else:
        head = node_x.next

    if node_x.next:
        node_x.next.prev = node_x.prev
    node_x.next = node_y
    node_x.prev = node_y.prev

    if node_y.prev:
        node_y.prev.next = node_x
    else:
        head = node_x

    node_y.prev = node_x

result = []
current = head
while current:
    result.append(current.val)
    current = current.next

print(' '.join(result))


