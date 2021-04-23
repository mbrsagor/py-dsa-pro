class Validation(object):

    def __init__(self, name, pin):
        self.name = name
        self.pin = pin
    
    def getValidations(self):
        pass

    def check(self):
        pass

    def namecheck(self):
        pass

    def pincheck(self):
        pass

    def confirm(self):
        pass


if __name__ == '__main__':
    myValidations = Validation("sagor", "sagor123")
