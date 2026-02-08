# https://www.nowcoder.com/practice/3790042b79114ae5bd9f6eccdaeadfcd
from collections import defaultdict

n = int(input())
index = defaultdict(list)

for doc_id in range(1, n + 1):
    parts = input().split()
    words = parts[1:]
    for word in set(words):
        index[word].append(doc_id)

m = int(input())
for _ in range(m):
    word = input().strip()
    if word in index:
        print(' '.join(map(str, index[word])))
    else:
        print()
