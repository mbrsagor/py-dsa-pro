numbers = range(1, 5)
number_filter = list(filter(lambda n: n == 4, numbers))
print(number_filter)

# random list
randomList = [1, 'a', 0, False, True, '0']
filteredList = filter(None, randomList)

print('The filtered elements are:')
for element in filteredList:
    print(element)

languages = ["python", "javascript", "java", "swift", "dart"]


def LanFunc(language):
    if language == "python":
        return True
    else:
        return False


myLan = filter(LanFunc, languages)
for lFnc in myLan:
    print(lFnc)
