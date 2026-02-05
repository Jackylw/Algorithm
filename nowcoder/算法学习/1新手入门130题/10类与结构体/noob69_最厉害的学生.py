# https://www.nowcoder.com/practice/b6e7a9ca04d8418b805b3b4b7d25b4d4
n = int(input())
best_stu = None
for _ in range(n):
    data = input().split()
    name = data[0]
    scores = list(map(int, data[1:]))
    total_score = sum(scores)
    if best_stu is None or total_score > best_stu[1]:
        best_stu = [name, total_score, scores]

print(f"{best_stu[0]} {' '.join(map(str, best_stu[2]))}")
