li = [i for i in range(1, 10 + 1)]
print(li)

li2 = [i * i for i in range(10)]
print(li2)

li3 = [i * i for i in range(10) if i % 2 == 0]
print(li3)

items = ["apple", "orange", "banana"]
item = [i.title() for i in items]
print(item)

li4 = [i.upper() for i in ["sagor", "ohi", "meg", "dhurbo"]]
print(li4)

my_name = "md. bozlur rosid sagor 2021"
name = [n for n in my_name if n.isdigit()]
print(name)
