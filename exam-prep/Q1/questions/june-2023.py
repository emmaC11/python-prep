import random, string

pool = string.digits + string.ascii_uppercase

class GuessMyEircode():
    def __init__(self):
        # self.__target = ''.join(random.choices(pool, k=7))
        self.__target = 'D02WC04'
        print('target value is: ', self.__target)

    def guess(self, code):
        if code == self.__target:
            return 0
        
        result = ''
        
        for letter in range(7):
            if code[letter] != self.__target[letter]:
                result += '1'
            else:
                result += '0'
        
        # print('code 7 bit string -> ', result)
        binary_7_output = int(result, 2)
        # print(' binary 7 bit number output - ', binary_7_output)
        return binary_7_output

def solve(game):
    # create our own list to iterate through and assign numbers
    current_list = list('aaaaaaa')

    for pos in range(7):
        for char in pool:
            current_list[pos] = char
            guess_str = ''.join(current_list)
            result = game.guess(guess_str)

            if result == 0:
                print('code found!!', result)
                print('solved target is', ''.join(current_list))
                return

            binary_bit = 1 << (6 - pos)

            if result & binary_bit == 0:
                break # break out of loop
    
    print('solved target is', ''.join(current_list))

    

guess = GuessMyEircode()
# guess.guess("D07WC02")
#self.__target = 'D02WC04'
solve(guess)

