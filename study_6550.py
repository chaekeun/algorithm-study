from sys import stdin
input = stdin.readline

def find(s, t):
    flag = "No"
    i = 0
    for char in t:
        if char == s[i]:
            i += 1
        if i == len(s):
            flag = "Yes"
            return flag
    return flag

while True:
    try:
        s, t = input().split()
        print(find(s,t))

    except:
        break

