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
    """
    Arithmetic Brownian motion object.
    Inputs:
        mu: real number, the constant for the linear drift
        sigma: real positive number, the standar deviation of the diffusion part
    """
    def __init__(self,mu,sigma): #,time,No_buckets):
        self.mu = mu
        self.sigma = sigma
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

    def sample_paths(self, initpoint, time, No_buckets, No_paths=1):
        self.time = time
        self.N = No_buckets
        self.initp = initpoint
        
        #equipartition
        self.dt = self.time/self.N
        #incrementos
        incr_mb = np.repeat(self.mu * self.dt,self.N) + np.sqrt(self.dt)*np.random.normal(0, self.sigma, size=(No_paths, self.N))
        print(np.transpose(np.array([self.initp]*No_paths)).shape)
        print(np.array([self.initp]*No_paths).shape)
        print(incr_mb)
        print(np.cumsum(incr_mb,axis=1))    
        print(incr_mb.shape)   

        # sample paths
        return np.vstack((np.array([self.initp]*No_paths),np.transpose(np.cumsum(incr_mb, axis=1))))
    
    def plot_sp (self, sample_paths):
        x = np.arange(0,self.time+self.dt,self.dt)
        y = sample_paths
        plt.plot(x,y)
        plt.title('Brownian motion')
        plt.xlabel('Time')
        plt.ylabel('Sample path')
        plt.show()

if __name__ == "__main__":        
    bm = BrownianMotion(0,1)
    
    bmsp = bm.sample_paths(0,1,1000,8)        
    print(bmsp.shape)

    bm.plot_sp(bmsp)        
            
            
            
            
            
            
            
            
            
            
            
