import sys
#sys.stdin=open("input.txt", "r")
a = list(input())
stack =[]

for i in a:
    if i.isdecimal():
        stack.append(int(i))
    else:
        if i == '+':
            c=stack[-2]+stack[-1]
            stack.pop()
            stack.pop()
            stack.append(c)
        elif i == '-':
            c=stack[-2]-stack[-1]
            stack.pop()
            stack.pop()
            stack.append(c)
        elif i == '*':
            c=stack[-2]*stack[-1]
            stack.pop()
            stack.pop()
            stack.append(c)
        else:
            c=stack[-2]/stack[-1]
            stack.pop()
            stack.pop()
            stack.append(c)

print(stack[-1])








