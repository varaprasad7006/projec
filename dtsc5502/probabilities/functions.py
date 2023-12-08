import numpy as np
import math

def factorial(n: int)-> int:
  # fact = 1 
  # for i in n:
  #   fact *= i

  # return fact
  # return math.factorial(n)
  return np.prod([i for i in range(1,n+1)])

def combination():
  pass

def exponential():
  pass

def compliment():
  pass
    