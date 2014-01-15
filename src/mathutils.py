import numpy as np
import pprint


def random_double():
  """
    return : a random double number
  """
  return np.random.rand()

def prob_based_rand(probs):
  """
    probs : prob list, sum equals to 1.0
    return : sample idx.
  """
  s = sum(probs)

  probs = map(lambda x : x / s , probs)
  cum_probs = np.cumsum(probs)
  
  r = random_double()
  
  for _it in range(len(cum_probs)):
    if cum_probs[_it] >= r :
      return _it
