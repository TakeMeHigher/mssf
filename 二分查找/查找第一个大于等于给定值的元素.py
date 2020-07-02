def search(li, low, high, target):
    while low <= high:
        mid = (low + high) // 2
        if li[mid] >= target:
            if mid == 0 or li[mid - 1] < target:
                return mid
            else:
                high = high - 1
        else:
            low = mid + 1


ll = [1, 3, 5, 9, 10]
print(search(ll, 0, len(ll) - 1, 7))
