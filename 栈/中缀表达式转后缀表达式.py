from 栈 import Stack


def prefix_to_postfix(str):
    prec = {}
    prec['('] = 1
    prec['+'] = 2
    prec['-'] = 2
    prec['*'] = 3
    prec['/'] = 3

    stack = Stack()
    data_list = []
    str_list = str.split()
    for item in str_list:
        if item == '(':
            stack.push(item)
        elif item == ")":
            while stack.peek() != '(':
                data_list.append(stack.pop())
        elif item in prec.keys() and item != '(':
            while not stack.is_empty() and prec.get(item, 0) <= prec.get(stack.peek(), 0):
                res = stack.pop()
                data_list.append(res)
            stack.push(item)
        else:
            data_list.append(item)

    while not stack.is_empty():
        data_list.append(stack.pop())

    return " ".join(data_list)


print(prefix_to_postfix("a * b + c * d"))
print(prefix_to_postfix("( a + b ) * c - ( d - e ) * ( f + g )"))
