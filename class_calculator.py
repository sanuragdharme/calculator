class ClassCalculator:

    def __init__(self, num):
        self.__num = num

    def __add__(self, other):
        if type(other) == int or type(other) == float:
            return self.get_num() + other
        elif type(other.get_num()) == int or type(other.get_num()) == float:
            return self.get_num() + other.get_num()

    def __sub__(self, other):
        if type(other) == int or type(other) == float:
            return self.get_num() - other
        elif type(other.get_num()) == int or type(other.get_num()) == float:
            return self.get_num() - other.get_num()

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            return self.get_num() * other
        elif type(other.get_num()) == int or type(other.get_num()) == float:
            return self.get_num() * other.get_num()

    def get_num(self):
        return self.__num
