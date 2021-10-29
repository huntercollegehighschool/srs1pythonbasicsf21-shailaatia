2
"""
Define a function twodigitodd that take a single integer argument (number). The function should return True if the number is a two digit odd number, and False if it is not.
"""

def twodigitodd(number):
  if number >= 10 and number > 99 and number/2 % 1 == 0:
    return False
  else:
   return True