# https://www.nowcoder.com/practice/006b7917d3784371a43cfbae01a9313d
n = int(input())
s = input()
for char in s:
    new_ascii = (ord(char) - ord('a') + n) % 26 + ord('a')
    print(chr(new_ascii), end="")