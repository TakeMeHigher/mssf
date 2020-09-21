from 栈 import Stack


def prefix_to_postfix(str):
    fu = {}
    fu['{'] = 1
    fu['['] = 2
    fu['('] = 3
    fu_s = "{[("
    fu_r = "}])"
    prec = {}
    prec['+'] = 2
    prec['-'] = 2
    prec['*'] = 3
    prec['/'] = 3

    stack = Stack()
    stack_fu = Stack()
    data_list = []
    str_list = str.split()
    for item in str_list:
        if item in fu_s:
            stack.push(item)
            stack_fu.push(item)
        elif item in fu_r:
            if stack_fu.is_empty():
                raise ValueError("表达式错误")
            if not match(item, stack_fu.peek()):
                raise ValueError("表达式错误")
            stack_fu.pop()
            res = stack.pop()
            while res != :
                data_list.append(res)
                res = stack.pop()
        elif item in prec.keys():
            while not stack.is_empty() and prec.get(item, 0) <= prec.get(stack.peek(), 0):
                res = stack.pop()
                data_list.append(res)
            stack.push(item)
        else:
            data_list.append(item)

    while not stack.is_empty():
        data_list.append(stack.pop())

    return " ".join(data_list)


def match(res, target):
    aa = '([{'
    bb = ')]}'

    return aa.index(res) == bb.index(target)


# print(prefix_to_postfix("a * b + c * d"))
print(prefix_to_postfix("( a + b ) * c - ( d - e ) * ( f + g )"))
