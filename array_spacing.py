# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 16:48:10 2025

@author: daniel.skrabacz
"""

#%% Import Libraries
import numpy as np

#%% Define Functions
def wl(f):
    return 3e8/f

def get_spacing(theta, frequency):
    return wl(frequency)/(1+np.cos(theta))

def theta2rad(theta):
    return theta*np.pi/180

def wave_res(L,C):
    return 1/np.sqrt(L*C)

#%% Run to get spacing over frequencies

frequencies = np.arange(1e9, 50e9, 1e9)

for x in frequencies:
    print(get_spacing(theta2rad(0),x)*1000)