import random, string

class GuessGame():
    def __init__(self, max):
        self.max = max
        self.__target = random.randint(0, max)
        print(f"target var is -> {self.__target}")

    def guess(self, number):
        if number == self.__target:
            print("0")
            return 0
        elif number > self.__target:
            print("1")
            return 1
        else:
            print("-1")
            return -1
        
def solve(game):
    low = 0
    high = game.max
    result = None

    while result != 0:
        midpoint = (low + high) // 2
        result = game.guess(midpoint)
        print(f"guess - {midpoint}, value - {result}")

        if result == 1:
            high = midpoint - 1

        elif result == -1:
            low = midpoint + 1
    print('guessed correctly -> ', midpoint)



my_game = GuessGame(11)
# my_game.guess(5)
solve(my_game)

