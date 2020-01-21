# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 12:41:30 2019

@author: Ranak Roy Chowdhury
"""
from matplotlib import pyplot as plt
import numpy as np

def SGD(x, iteration):
    result = [x]
    for i in range(iteration - 1):
        x = x - g(x)
        result.append(x)
    return result

def g(x):
    result = 0
    for i in range(1, 11):
        result += np.log(np.cosh(x + 2/np.sqrt(i)))
    return result/10

if __name__ == "__main__":
    x = -2
    iteration = 20
    result = SGD(x, iteration)
    l = np.arange(0, iteration, 1)
    plt.plot(l, result, label='x_n vs x')
    plt.legend(loc = 'lower left', fontsize='large')