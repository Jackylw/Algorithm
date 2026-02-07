# https://www.nowcoder.com/practice/bd911c77a1ed4e289a0699fa7df23b6c
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    if not headA or not headB:
        return None

    pA, pB = headA, headB

    while pA != pB:
        pA = pA.next if pA else headB
        pB = pB.next if pB else headA

    return pA


# 你不需要关心主函数内容！
def main():
    # 读入数据
    lenA, lenB, commonLen = map(int, input().split())

    # 读入链表A的独立部分
    valuesA = list(map(int, input().split()))
    # 读入链表B的独立部分
    valuesB = list(map(int, input().split()))
    # 读入公共部分
    valuesCommon = list(map(int, input().split()))
    nodesCommon = []
    if (commonLen == 0):
        nodesCommon = []
    else:
        nodesCommon = [ListNode(x) for x in valuesCommon]

    # 构建链表
    nodesA = [ListNode(x) for x in valuesA]
    nodesB = [ListNode(x) for x in valuesB]

    # 连接链表A的独立部分
    for i in range(len(nodesA) - 1):
        nodesA[i].next = nodesA[i + 1]

    # 连接链表B的独立部分
    for i in range(len(nodesB) - 1):
        nodesB[i].next = nodesB[i + 1]

    # 连接公共部分
    for i in range(len(nodesCommon) - 1):
        nodesCommon[i].next = nodesCommon[i + 1]

    # 设置头节点并连接公共部分
    headA = None
    headB = None

    if len(nodesA) > 0:
        headA = nodesA[0]
        if len(nodesCommon) > 0:
            nodesA[-1].next = nodesCommon[0]
    elif len(nodesCommon) > 0:
        headA = nodesCommon[0]

    if len(nodesB) > 0:
        headB = nodesB[0]
        if len(nodesCommon) > 0:
            nodesB[-1].next = nodesCommon[0]
    elif len(nodesCommon) > 0:
        headB = nodesCommon[0]

    # 调用函数获取结果
    result = getIntersectionNode(headA, headB)

    # 输出结果
    if result is None:
        print("null")
    else:
        print(result.val)


if __name__ == "__main__":
    main()