import numpy as np

class LogTransformer:
    def __init__(self, constant=1e-5):
        self.constant = constant

 
   
   
   
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return np.log1p(X + self.constant)

       