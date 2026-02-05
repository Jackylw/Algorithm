# https://www.nowcoder.com/practice/eaf21203b61b4a689987fdc165d00dfc
n = input()
month = int(n[-2:])
if month == 12 or 1 <= month <= 2:
    print("winter")
elif 3 <= month <= 5:
    print("spring")
elif 6 <= month <= 8:
    print("summer")
elif 9 <= month <= 11:
    print("autumn")