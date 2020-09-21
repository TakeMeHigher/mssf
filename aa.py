import sys


# str = input()
# print(str)
def get_fix(li: list):
    dic = {"count": 0}
    first = li[0]
    for i in range(1, len(li)):
        all = True
        if first[dic['count']] not in li[i]:
            all = False
        if all == True:
            dic['count'] += 1
    return first[: dic['count']]


print(get_fix(["fwler", "flow", "flight"]))

