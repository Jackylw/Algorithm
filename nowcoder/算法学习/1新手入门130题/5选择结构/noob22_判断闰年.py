# https://www.nowcoder.com/practice/a7bcbe3cb86f435d9617dfdd20a16714
year = int(input())
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("yes")
else:
    print("no")
