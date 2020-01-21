# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 11:49:11 2019

@author: Ranak Roy Chowdhury
"""
from matplotlib import pyplot as plt
import numpy as np

def Q(x, y):
    return f(y) + f_prime(y)*(x-y) + 0.5*(x-y)**2

def f(x):
    return (np.log(np.cosh(x)))

def f_prime(x):
    return (np.tanh(x))
    
if __name__ == "__main__":
    x = np.arange(-10, 10, 0.1)        
    plt.plot(x, f(x), label='f(x)')
    plt.plot(x, Q(x, -2), label='Q(x,-2)')
    plt.plot(x, Q(x, 3), label='Q(x,3)')
    plt.legend(loc = 'upper right', fontsize='large')