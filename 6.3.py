# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 13:47:34 2019

@author: Ranak Roy Chowdhury
"""
import math
import numpy as np


def readFiles():
    filename = "spectX.txt"
    X = []
    with open(filename) as f:
        for line in f:
            line = line.split()
            l = []
            for i in line:
                l.append(int(i))
            X.append(l)
    
    filename = "spectY.txt"
    Y = []
    with open(filename) as f:
        for line in f:
            line = line.split()
            Y.append(int(line[0]))
    
    return X, Y
    
    
def product(n, p, X_t):
    ones = [1] * n
    sub = [ones_i - p_i for ones_i, p_i in zip(ones, p)]
    power = [pow(sub_i, X_t_i) for sub_i, X_t_i in zip(sub, X_t)]
    result = np.prod(power)
    return result    
    

def logLikelihood(X, Y, p, T, n):
    total = 0
    for t in range(T):
        if Y[t] == 1:
            total += math.log(1 - product(n, p, X[t]))
        else:
            total += math.log(product(n, p, X[t]))
    return total/T
    

def Expectation(X, Y, p, T, n):
    P_ti = []
    for t in range(T):
        deno = 1 - product(n, p, X[t])
        nume = [Y[t] * X_t_i * p_i for p_i, X_t_i in zip(p, X[t])]
        res = [nume_i / deno for nume_i in nume]
        P_ti.append(res)
    return P_ti
    

def Maximization(P_ti, X_col_totals):
    P_ti_col_totals = [sum(p_i) for p_i in zip(*P_ti)]
    p = [p_i / x_i for p_i, x_i in zip(P_ti_col_totals, X_col_totals)]
    return p

        
def prediction(X, Y, p, T, n):
    result = []
    for t in range(T):
        pred = 1 - product(n, p, X[t])        
        if pred <= 0.5:
            result.append(0)
        else:
            result.append(1)
    match = sum(len(set(i))==1 for i in zip(result, Y))
    return T - match
    

def EM(X, Y, p, T, n, iteration):
    ll = []
    mistakes = []
    X_col_totals = [sum(x) for x in zip(*X)]
    for k in range(iteration):
        log_likelihood = logLikelihood(X, Y, p, T, n)
        ll.append(log_likelihood)
        mistake = prediction(X, Y, p, T, n)
        mistakes.append(mistake)
        P_ti = Expectation(X, Y, p, T, n)
        p = Maximization(P_ti, X_col_totals)
    return ll, mistakes            
    

def printResult(ll, mistakes, position):
    for pos in position:
        print(mistakes[pos])
    for pos in position:
        print(ll[pos])
        
    
if __name__ == "__main__":
    print("Read Files")
    X, Y = readFiles()
    T = 267
    n = 23
    p = [0.05] * n
    iteration = 257
    ll, mistakes = EM(X, Y, p, T, n, iteration)
    pos = [0, 1, 2, 4, 8, 16, 32, 64, 128, 256]
    printResult(ll, mistakes, pos)