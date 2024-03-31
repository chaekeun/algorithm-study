from sys import stdin
input = stdin.readline

n = int(input())
word = input()
a = []
temp = '0'

for char in word:
    c = ord(char)
    if not (c >= 48 and c <= 57):
        a.append(int(temp))
        temp = "0"
        continue
    temp += char

print(sum(a))
    