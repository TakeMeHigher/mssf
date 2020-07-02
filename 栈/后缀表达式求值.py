from 栈 import Stack


def postfix_eval(str):
    stock = Stack()

    str_list = str.split()
    for data in str_list:
        if data in "0123456789":
            stock.push(int(data))
        else:
            res1 = stock.pop()
            res2 = stock.pop()
            res = do_math(res1, res2, data)
            stock.push(res)
    return stock.pop()


def do_math(res1, res2, op):
    if op == '+':
        return res1 + res2
    elif op == "-":
        return res1 - res2
    elif op == "*":
        return res1 * res2
    else:
        return res1 / res2


if __name__ == '__main__':
    aa = postfix_eval("7 8 + 3 1 + *")
    print(aa)
