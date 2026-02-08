# https://www.nowcoder.com/practice/46f68af83db74b709a788dedb656c5f9
from collections import defaultdict

n = int(input())
# 前缀 洲 count
maps = defaultdict(int)
for _ in range(n):
    city, continent = input().split()
    maps[(city[:2], continent)] += 1

ans = 0
for (city, continent), count in maps.items():
    if city != continent and (continent, city) in maps.keys():
        ans += count * maps[(continent, city)]

print(ans // 2)
