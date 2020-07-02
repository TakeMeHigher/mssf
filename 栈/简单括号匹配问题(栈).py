from 栈 import Stack


def pipei(str):
    stock = Stack()
    blance = True
    index = 0

    while index < len(str) and blance:
        if str[index] == '(':
            stock.push(str[index])
        else:
            if stock.is_empty():
                blance = False
            else:
                stock.pop()
        index += 1

    if stock.is_empty() and blance:
        return True
    else:
        return False


print(pipei("((((())))))"))
print(pipei("((((()))))"))
