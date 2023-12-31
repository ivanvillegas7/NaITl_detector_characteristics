# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 15:27:22 2023

@author: Iván
"""

import numpy as np

from typing import List

import scipy.optimize as opt

def gaussian(x: np.array(float), mu: float, sigma: float, A:float):
    
    return A*np.exp(-(x-mu)**2/(2*sigma**2))/(sigma*np.sqrt(2*np.pi))

def fit(x: np.array(float), y: np.array(float), err_y: np.array(float)):
    
    params = opt.curve_fit(gaussian, xdata=x, ydata=y, p0=[1000, 100, 5], sigma=err_y)
    
    mu: float = params[0][0]
    
    sigma: float = params[0][1]
    
    A: float = params[0][2]
    
    cov: List[np.array(float)] = params[1]
    
    return (mu, sigma, A, np.sqrt(cov[0, 0]), np.sqrt(cov[1, 1]))

def fit2(x: np.array(float), y: np.array(float), err_y: np.array(float)):
    
    params = opt.curve_fit(gaussian, xdata=x, ydata=y, p0=[150, 50, 5], sigma=err_y)
    
    mu: float = params[0][0]
    
    sigma: float = params[0][1]
    
    A: float = params[0][2]
    
    cov: List[np.array(float)] = params[1]
    
    return (mu, sigma, A, np.sqrt(cov[0, 0]), np.sqrt(cov[1, 1]))