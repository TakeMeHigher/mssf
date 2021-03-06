def search(li, low, high, target):
    while low <= high:
        mid = (low + high) // 2

        if li[mid] > target:
            high = mid - 1
        elif li[mid] < target:
            low = mid + 1

        else:
            if mid == 0 or li[mid - 1] != target:
                return mid
            else:
                high = high - 1


ll = [1, 3, 4, 5, 6, 8, 8, 8, 11, 18]

print(search(ll, 0, len(ll) - 1, 8))
