"""Simple example of linear searchsearch = [64, 34, 25, 12, 22, 11, 90]search_val = 10 in search:return search_val"""def linear_search(item, value):    for i in range(len(item)):        if value == item[i]:            print(f"The element {value} is found of index {i}")            break    else:        print(f"Sorry! The element {value} is not found.")_item = [10, 12, 15, 100, 30, 6, 90]val = int(input("Enter your search value: "))linear_search(_item, val)