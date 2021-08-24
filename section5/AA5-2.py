import sys
#sys.stdin=open("input.txt", "r")
s = input()
cnt = 0
stack = []

for i in range(len(s)):
    if s[i] == '(':
        stack.append(s[i])
        
    else:
        stack.pop()
        
        if s[i-1]=='(':
            cnt += len(stack)
        else:
            cnt += 1

print(cnt)
