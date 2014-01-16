import numpy as np
from numpy.linalg import det
from numpy.linalg import inv 
from numpy import eye
from numpy import exp
from numpy import pi
from numpy import dot
from numpy import transpose
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

def prob_based_rand_dict(probs_dict):
  """
    probs : prob dict, sum equals to 1.0
    return : sample idx.
  """
  s = sum(probs_dict.values()) 
  for _i in probs_dict.keys():
    probs_dict[_i] = probs_dict[_i] / s

  _t = 0.0
  for _key in probs_dict.keys():
    _t += probs_dict[_key]
    probs_dict[_key] = _t

  r = random_double()
  
  for _key in probs_dict.keys():
    if probs_dict[_key] >= r :
      return _key

def gauss_comp(X, mu, sigma, mode):
  """
    X : a list of data 
    mu : mu in guass distribution
    sigma : convariance matrix
    mode :  string, NEW or OLD
    return : a prob value
  """
  if mode == 'NEW' :
    prob = 1.0 / (2*pi)*det(inv(2.0*eye(2)))**(1/2.0) * exp(-1/2.0*dot(transpose(X), dot(1/2.0*eye(2), X)))
    return prob[0][0]
  elif mode == 'OLD': 
    prob = 1.0 / (2*pi)*exp(-1/2.0*dot((X-mu), transpose(X-mu)))
    return prob[0][0]
  else :
    print " [ ERROR ] Unknown Mode : %s" % (mode)

