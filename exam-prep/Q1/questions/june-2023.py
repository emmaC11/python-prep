import random, string

pool = string.digits  + string.ascii_uppercase

class GuessMyEircode:
    def __init__(self):
        # self.__target = ''.join(random.choices(pool, k=7))
        self.__target = 'D02WC04'
        print("random code", self.__target)

    def guess(self, code):
        if code == self.__target:
            print("CODE FOUND")
            return 0
        
        bits = ''

        for letter in range(len(self.__target)):
            if code[letter] != self.__target[letter]:
                bits += "1"
            else:
                bits += "0"

        print("bits output", bits)
        return int(bits)
   

guess = GuessMyEircode()
guess.guess("D07WC02")



