# 3 step anatomy of a question
# 1 - create a class that hides secret random value '_target' & a method that gives you a 'hint' (not answer just warmer colder)
# 2 - write a solve/find function that uses the hints to figure out the secret, printing each attempt
# 3 - explain big-O complexity of 4-5 listen algorithims

import random, math

class Location:
  
  def __init__(self, maxi):
    self.maxi = maxi
    self.__target = tuple(random.randint(-maxi, maxi) for _ in range(3))
    print("target output -> ", self.__target)

  def distance(self, other):
    return math.sqrt(sum((a-b)**2 for a,b in zip(self.__target, other)))
    

def find(a):
  guesses = [0,0,0]


  for axis in range(3):
    low, high = -a.maxi, a.maxi

    while low < high:
      midpoint = (high + low) // 2

      t1 = guesses[:]
      t2 = guesses[:]

      t1[axis] = midpoint
      t2[axis] = midpoint + 1

      if a.distance(t1) <= a.distance(t2):
        high = midpoint
      else:
        low = midpoint + 1

    guesses[axis] = low
    print(tuple(guesses))
    

loc = Location(5)
# loc.distance((10,10,10))
find(loc)




