import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_confidence(self) :
        nv = 0 
        for j in range(100) : 
            mean, bar = hypergeom_mean( 50, 4, 3, 12 )
            if np.abs( mean - 4*(3/12) )<bar : nv = nv + 1

        prob = 0.9 
        bar = np.sqrt( prob*(1-prob) / 100 )*scipy.stats.norm.ppf( (0.99+1)/2 )
        self.assertTrue( np.abs( nv/100 - prob)<bar, "Your confidence limits have not been computed correctly" )
        
    def test_mean(self) :
        for M in range(2,4) :
           for N in range(5,7) : 
              for R in range(1,N) : 
                 mean, conf = hypergeom_mean(100, M, R, N)
                 prob = R/N
                 var = M*prob*((N-R)/N)*(N-M)/(N-1)
                 bar = np.sqrt(var/100)*scipy.stats.norm.ppf( (0.99 + 1) / 2 )
                 self.assertTrue( np.fabs( mean - M*prob )<bar, "The distribution you are sampling the mean from from does not appear to be correct" )
