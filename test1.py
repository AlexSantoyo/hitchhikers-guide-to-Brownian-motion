#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 15:27:38 2020

@author: Alex y Fide
"""

"""
The objective is to create a class for Brownian motion.
The first use of this class is to generate sample paths of various processes related to BM, 
for example:
    - Non standard Brownian motion
    - Brownian Drift
    - Non intersecting Brownian motion
    - Geometric Brownian motion
    - Two dimensional Brownian motion
    - Local time surface
"""

"""
This first attempt is to create sample paths of BM, bridge and watermelon
"""

import numpy as np
import matplotlib.pyplot as plt
import random as rnd

class BrownianMotion:
    def __init__(self,drift,stdev): #,time,No_buckets):
        self.mu = drift
        self.sigma = stdev
        self.initp = 0
        self.time = []
        self.N = []
    
    def sample_path(self,initpoint,time,No_buckets):
        self.time = time
        self.N = No_buckets
        self.initp = initpoint
        
        #equipartición
        self.dt = self.time/self.N
        #incrementos
        incr_mb = np.repeat(self.mu * self.dt,self.N) + np.sqrt(self.dt)*np.random.normal(0, self.sigma, self.N)
        # trayectoria
        return np.append(self.initp,np.cumsum(incr_mb))

    def plot_sp (self, sample_path):
        x = np.arange(0,self.time+self.dt,self.dt)
        y = sample_path
        plt.plot(x,y)
        plt.title('Brownian motion')
        plt.xlabel('Time')
        plt.ylabel('Sample path')
        plt.show()
        
bm = BrownianMotion(0,5)        
bmsp = bm.sample_path(0,1,1000)        
bm.plot_sp(bmsp)        
        
        
        
        
        
        
        
        
        
        
        
