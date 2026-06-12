import random, string, math

pool = string.digits

class GuessMyPin():
    def __init__(self, digits):
        self.digits = digits
        self.__target = ''.join(random.choices(pool, k=digits))
        # self.__target = '12345'
        print(f"target is: {self.__target}")

    def guess(self, number):
        if number == self.__target:
            return 0
        incorrect_digits = 0
        for pos in range(self.digits):
            if number[pos] != self.__target[pos]:
                incorrect_digits += 1

        print(f"incorrect digit count: {incorrect_digits}")
        return incorrect_digits



my = GuessMyPin(5)
my.guess('13534')