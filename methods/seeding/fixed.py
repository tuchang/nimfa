import scipy.sparse as sp
import numpy as np

class Fixed(object):
    """
    Fixed factorization. This is the option to completely specify the initial factorization by passing values for 
    matrix factors.  
    """

    def __init__(self):
        self.name = "fixed"
        
    def _set_fixed(self, *factors):
        """Set initial factorization."""
        self.factors = factors
        for f in factors:
            f = np.matrix(f) if not sp.isspmatrix(f) else f.copy() 
        
    def initialize(self, *args, **kwargs):
        """
        Return fixed matrix factors.
        """
        return self.factors
    
    def __repr__(self):
        return "fixed.Fixed()"
    
    def __str__(self):
        return self.name