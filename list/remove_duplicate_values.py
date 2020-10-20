def remove_duplicate_values(arr, num):
    if num == 0 or num == 1:
        return num

    temp = list(range(num))

    j = 0
    for i in range(0, num - 1):
        if arr[i] != arr[i + 1]:
            temp[j] = arr[i]
            j += 1

    temp[j] = arr[num - 1]
    j += 1

    for i in range(0, j):
        arr[i] = temp[i]
    return j


items = [1, 2, 2, 3, 4, 4, 4, 5, 5]
val = len(items)
_val = remove_duplicate_values(items, val)
for v in range(_val):
    print((items[v]), end=" ")
