# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 12:34:58 2019

@author: Ranak Roy Chowdhury
"""

from matplotlib import pyplot as plt
import numpy as np

def g(x):
    result = 0
    for i in range(1, 11):
        result += np.log(np.cosh(x + 2/np.sqrt(i)))
    return result/10

if __name__ == "__main__":
    x = np.arange(-10, 10, 0.1)        
    plt.plot(x, g(x), label='g(x)')
    plt.legend(loc = 'upper left', fontsize='large')
    