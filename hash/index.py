class Person(object):
    """
    Here the `hash` method returns the hash value of an object if it has one.
    return:: hash() Parameters
    """
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def __eq__(self, other):
        return self.age == other.age and self.name == other.name

    def __hash__(self):
        print('The hash is:')
        return hash((self.age, self.name))


person = Person(26, 'Sagor')
print(hash(person))
person2 = Person(29, 'Masba')
print(hash(person2))

if person == person2:
    print("They are same")
else:
    print("They are different")
