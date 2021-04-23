class MyHas(object):

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __eq__(self, other):
        return self.username == other.username and self.password == other.password

    def __hash__(self):
        return hash((self.username, self.password))


MyHas = MyHas(25, 'Jon')
print(hash(MyHas))
MyHas2 = MyHas(28, 'Deo')
print(hash(MyHas2))

if MyHas == MyHas2:
    print("They are same user")
else:
    print("They are different user")
