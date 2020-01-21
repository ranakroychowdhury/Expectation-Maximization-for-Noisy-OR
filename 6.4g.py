# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 12:28:20 2019

@author: Ranak Roy Chowdhury
"""

from matplotlib import pyplot as plt
import numpy as np

def newton(x, iteration):
    result = [x]
    for i in range(iteration - 1):
        x = x - np.tanh(x)*np.cosh(x)*np.cosh(x)
        result.append(x)
    return result
    
if __name__ == "__main__":
    x = -2
    iteration = 20
    result = newton(x, iteration)
    l = np.arange(0, iteration, 1)
    plt.plot(l, result, label='x_n vs x for x_0 = -2')
    
    x = 3
    iteration = 20
    result = newton(x, iteration)
    plt.plot(l, result, label='x_n vs x for x_0 = 3')
    
    plt.legend(loc = 'upper left', fontsize='large')