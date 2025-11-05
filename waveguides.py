# -*- coding: utf-8 -*-
"""
August 26, 2025

author: daniel.skrabacz

"""

 #%% Import Libraries
 
import numpy as np
import matplolib.pyplot as plt

#%% Functions

c=3e8

def cutFreq(a,b,m=1,n=0):
    return 3e8/(2*np.pi)*np.sqrt((m*np.pi/a)**2 + (n*np.pi/b)**2)

def ads(a,er,d, p): # for dielectric filled waveguide, calculate new effective width
    return (a/np.sqrt(er)) - d**2/(0.95*p)

def guideWL(er, f, a):
    den = (er*(2*np.pi*f)**2)/c**2 -(np.pi/a)**2
    return 2*np.pi/np.sqrt(den)

def viaSizeSIW(gWL):
    return gWL/5

def pitchSIW(d):
    return 2*d

def meters2mils(x):
    return x*39370.1

def mils2meters(x):
    return x/39370.1

def SIWdesign(a,er,designFreq):
    """
    Full SIW design focusing on the cross sectional area.
    
    For a SIW, the fundamental mode is TE10.
    In designing the SIW, you don't really need the b term, because n=0...
    
    Parameters
    ----------
    a : width (meters)
    b : height (meters)
    er : relative permittivity
    designFreq : frequency you are targeting the design to.

    Returns
    -------
    via sizes, via pitches, and effective width (ads).

    """
    gwl = guideWL(er, designFreq, a);
    d = gwl/5; print('Via diameter needs to be less than:', d)
    p = 2*d; print('Via pitch needs to be less than:', p)
    d_choice = input('Pick a via diameter (d) that is less than calculated:', d)
    p_choice = input('Pick a via pitch (p) that is less than calculated:', p)
    effective_width = ads(a, er, d_choice, p_choice)
    return d_choice, p_choice, effective_width


#%% Test out the functions

a = 0.02286 # meters
b = 0.01016 # meters
print(cutFreq(a,b)) # This should return 6.56GHz for WR90 cutoff frequency
print(c/(2*a)) # simplified calculation because m=1 and n=0


print(guideWL(3, 26.5e9, 0.01067))


#%% SIW design tool









