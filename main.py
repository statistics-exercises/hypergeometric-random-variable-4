import numpy as np 
import scipy.stats 

def hypergeom_mean( nsamples, M, R, N ) : 
  mean = 0 
  # Your code goes here 
  return mean, confidence_limit
  
  
  
# This is just to test your function.  You should not need to adjust anything
# from this point in the code onwards
mymean, mybar = hypergeom_mean( 100, 4, 3, 12 )
print("100 samples were taken from a hypergeometric distribution.")
print("The mean value obtained was", mymean)
print("If this mean is resampled 90% of the resamples should fall within", mybar, "of this value")
