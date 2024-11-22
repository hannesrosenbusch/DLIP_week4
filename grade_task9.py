from task import *
import numpy as np

def test_sigmoid():
  assert sigmoid.__name__ == '<lambda>', "sigmoid was not defined as a lambda expression"
  assert sigmoid(0) == 1/2
  assert np.abs(sigmoid(-np.log(np.arange(5,10))) - np.array([1/i for i in range(6,11)])).max() < 1e-12
  
