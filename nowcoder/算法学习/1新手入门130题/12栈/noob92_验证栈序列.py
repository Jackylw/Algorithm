# https://www.nowcoder.com/practice/d3178fe362dd4810b577c77c9e128fc5
q = int(input())
for _ in range(q):
    n = int(input())
    push_list = list(map(int, input().split()))
    pop_list = list(map(int, input().split()))
    check_tmp = []
    j = 0 # pop_list的索引
    for x in push_list:
        check_tmp.append(x)
        while check_tmp and check_tmp[-1] == pop_list[j]:
            check_tmp.pop()
            j += 1
    print('Yes' if not check_tmp else 'No')