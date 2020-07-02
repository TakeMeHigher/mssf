def func(num):
    ll = []
    while num > 0:
        ll.append(str(num % 2))
        num = num // 2
    ll.reverse()
    return ''.join(ll)


def divideBy2(decNumber):
    ll = []

    while decNumber > 0:
        rem = decNumber % 2
        ll.append(rem)
        decNumber = decNumber // 2

    binString = ""
    while ll:
        binString = binString + str(ll.pop())

    return binString


print(divideBy2(42))
