# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 13:12:27 2019

@author: courtney
"""

'''
Creating histogram images
'''

import numpy as np
import matplotlib.pyplot as plt
import os

os.chdir('/home/courtney/Desktop/practice/chips')

ubins = []
bins = []

uim01 = plt.imread('glacier003.2018-08-01.tif')
uim07 = plt.imread('glacier003.2018-08-07.tif')
uim13 = plt.imread('glacier003.2018-08-13.tif')
uim19 = plt.imread('glacier003.2018-08-19.tif')
uim25 = plt.imread('glacier003.2018-08-25.tif')

'''ubins = [0 to 255]'''

uim0107 = uim01-uim07
uim0713 = uim07-uim13
uim1319 = uim13-uim19
uim1925 = uim19-uim25

'''bins = [-128 to 128]'''

im0107 = np.int8(uim0107)
im0713 = np.int8(uim0713)
im1319 = np.int8(uim1319)
im1925 = np.int8(uim1925)

for n in range(256):
    ubins.append(n)

for n in range(-128, 128, 1):
    bins.append(n)

figure1, (ax11, ax12, ax13, ax14) = plt.subplots(nrows=1, ncols=4, figsize=(24, 4))
ax11.hist(im0107.ravel(), bins)
ax12.hist(im0713.ravel(), bins)
ax13.hist(im1319.ravel(), bins)
ax14.hist(im1925.ravel(), bins)


figure2, (ax21, ax22, ax23, ax24) = plt.subplots(nrows=1, ncols=4, figsize=(24, 4))
ax21.hist(uim0107.ravel(), ubins)
ax22.hist(uim0713.ravel(), ubins)
ax23.hist(uim1319.ravel(), ubins)
ax24.hist(uim1925.ravel(), ubins)
