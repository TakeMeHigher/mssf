prec = {}
prec['('] = 1
prec['+'] = 2
prec['-'] = 2
prec['*'] = 3
prec['/'] = 3

from 栈 import Stack


def get_resut(str):
    stock_num = Stack()
    stock_fh = Stack()

    ll = str.split(" ")

    for i in ll:
        if i in prec:
            while stock_fh.size() > 0 and prec[stock_fh.peek()] >= prec[i]:
                fh = stock_fh.pop()
                num2 = stock_num.pop()
                num1 = stock_num.pop()
                print(f'{fh} {num2} {num1}')
                stock_num.push(do_math(num1, num2, fh))
            stock_fh.push(i)
        else:
            if i.isdigit():
                stock_num.push(int(i))
            else:
                raise ValueError('must be number')

    while not stock_fh.is_empty():
        fh = stock_fh.pop()
        num2 = stock_num.pop()
        num1 = stock_num.pop()
        print(f'{fh} {num2} {num1}')
        stock_num.push(do_math(num1, num2, fh))
    return stock_num.pop()


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
    resut = get_resut("2 + 4 * 5 - 6 + 7 * 9")
    print(resut)
