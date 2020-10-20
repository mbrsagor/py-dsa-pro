def remove_duplicate_values(item, value):
    if value == 0 or value == 1:
        return value

    temp = list(range(value))

    # Start traversing elements
    j = 0
    for i in range(0, value - 1):
        if item[i] != item[i + 1]:
            temp[j] = item[i]
            j += 1

    temp[j] = item[value - 1]
    j += 1

    for i in range(0, j):
        item[i] = temp[i]
    return j


items = [1, 2, 2, 3, 4, 4, 4, 5, 5]
val = len(items)
val = remove_duplicate_values(items, val)
for i in range(val):
    print((items[i]), end=" ")
