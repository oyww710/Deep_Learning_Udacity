import numpy as np

def cross_entropy(Y, P):
    Y = np.float_(Y)
    P = np.float_(P)
    return -np.sum(Y * np.log(P) + (1 - Y) * np.log(1 - P))
  
  
# Trying for Y=[1,0,1,1] and P=[0.4,0.6,0.1,0.5].
# The correct answer is
# 4.8283137373
# And your code returned
# 4.8283137373
