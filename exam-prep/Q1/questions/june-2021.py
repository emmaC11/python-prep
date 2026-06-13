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

        return incorrect_digits
    
def solve(game):
    current_pin = list('xxxxx')
    current_incorrect_count = game.guess(''.join(current_pin))
    for pos in range(len(current_pin)):
        for digit in pool:
                current_pin[pos] = digit
                current_pin_str = ''.join(current_pin)
                incorrect_count = game.guess(current_pin_str)

                if incorrect_count == 0:
                    print('pin found', current_pin_str)
                    return

                if incorrect_count < current_incorrect_count:
                    print('match found - ', current_pin_str)
                    break
        current_incorrect_count = incorrect_count
        
    print('pin found: ', current_pin_str)






my = GuessMyPin(5)
# my.guess('13534')
solve(my)