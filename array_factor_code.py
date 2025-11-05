# -*- coding: utf-8 -*-
"""
Created on Wed Sep 17 11:45:36 2025

@author: daniel.skrabacz
"""
#%% Import Libraries
import numpy as np
import matplotlib.pyplot as plt

#%% Define constants

frequency = 20e9;
wavelength = 3e8/frequency

d = wavelength/2
k = 2* np.pi/wavelength


θ = np.deg2rad(np.arange(-180, 180, 0.001, dtype=np.float64));
φ = np.deg2rad(np.arange(-180, 180, 0.001, dtype=np.float64));

eRI = 1; # isotropic radiator
myPattern = np.ones(len(θ))
# xRI = eRI* np.sin(θ) * np.cos(φ);
# yRI = eRI* np.sin(θ) * np.sin(φ);
# zRI = eRI* np.cos(φ)
linear_array_length = 7
w = np.ones(linear_array_length);
r = d*np.arange(linear_array_length)

AF = np.zeros_like(θ, dtype=complex)

for n in range(len(w)):
    AF += w[n] * np.exp(1j* k *r[n] *np.sin(θ))

AF_mag = np.abs(AF)
AF_norm = AF_mag/AF_mag.max()
AF_dB   = 20*np.log10(AF_norm + 1e-12)  # add tiny offset to avoid log(0)
print(max(AF_dB))
AF_dB = np.clip(AF_dB, -40, 0)
AF_dB_shift = AF_dB - AF_dB.min()

fig, ax = plt.subplots(
    dpi=200,
    subplot_kw={'projection': 'polar'}
)
ax.plot(θ, AF_dB_shift, lw=1.5)
ax.set_rmax(40)
ax.set_rticks(np.linspace(0, AF_dB_shift.max(), 5))
ax.set_theta_zero_location('N')
ax.set_theta_direction(-1)
ax.grid(True, ls='--', alpha=0.5)
# ax.set_title('Array Factor (dB, shifted to positive)', va='bottom')
plt.show()
