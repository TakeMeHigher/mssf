def js(li):
    if len(li) <= 0:
        return
    aa = [0] * (max(li) + 1)

    for i in li:
        aa[i] += 1
    # 累加操作 获取当前小于等于当前值的数量num 也就是该值在 排序列索的索引 = num -1
    for i in range(1, len(aa)):
        aa[i] = aa[i - 1] + aa[i]

    ss = [0] * len(li)
    for i in li:
        index = aa[i] - 1
        ss[index] = i
        aa[i] -= 1
    print(ss)
    li[:] = ss


ll = [1, 6, 3, 4, 5, 6]
js(ll)
print(ll)
