from 栈 import Stack


def pipei(str):
    stack = Stack()
    blance = True
    index = 0

    while index < len(str) and blance:
        if str[index] in "({[":
            stack.push(str[index])
        else:
            if stack.is_empty():
                blance = False
            else:
                if match(stack.peek(), str[index]):
                    stack.pop()
        index += 1

    if stack.is_empty() and blance:
        return True
    else:
        return False


def match(res, target):
    aa = '([{'
    bb = ')]}'

    return aa.index(res) == bb.index(target)


print(pipei('{{([][])}()}'))
print(pipei('[{()]'))
