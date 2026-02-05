# https://www.nowcoder.com/practice/1a7a7c8d721547a29107cf02330ffe72
T = int(input())
for _ in range(T):
    lengths = [len(input()) for _ in range(4)]
    selected = ['A', 'B', 'C', 'D']

    min_len = min(lengths)
    max_len = max(lengths)
    min_count = lengths.count(min_len)
    max_count = lengths.count(max_len)

    # 既有一个最短长度+一个最长长度，属于参差不齐形状
    if min_count == 1 and max_count != 1:
        print(selected[lengths.index(min_len)])
    elif max_count == 1 and min_count != 1:
        print(selected[lengths.index(max_len)])
    else:
        print('C')



