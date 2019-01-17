# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 08:15:21 2018

@author: courtney
"""

import subprocess
import os
import matplotlib.pyplot as plt

init_path = r"/home/courtney/Desktop/practice/"
os.chdir(init_path)

glaciers_txt = init_path + "glaciers.txt"
mosaics_path = init_path + "mosaics50m/"
dated_directories = sorted(os.listdir(mosaics_path))  #TODO formatting


def Get_vrt(date):
    '''
    Returns the .vrt file associated with a particular
    date in time in which radar imagery was captured
    '''
    for file in os.listdir(date):
        if file.endswith('.vrt'):
            vrt = file
    return vrt


def Create_chips(vrt, date, glacier_info):
    '''
    Cuts multiple glacier "chips" from a .vrt file whose corner
    coordinates are specified from the text file, "glacier_info"
    '''
    lines = [line.rstrip('\n') for line in open(glacier_info)]
    for line in lines:
        glacier_coords = line.split(' ')
        subprocess.call(['gdalwarp', '-t_srs', 'EPSG:3413', '-te', glacier_coords[1], glacier_coords[2], glacier_coords[3], glacier_coords[4], '-tr', '50', '50', vrt, glacier_coords[0]+'.'+date+'.tif'])

for date in dated_directories:
    os.chdir(mosaics_path+date)
    path = os.getcwd()
    vrt = Get_vrt(path)
    Create_chips(vrt, date, glaciers_txt)
    
'''
subprocess.call("./cutchips", shell=True)

images = []

for tif in os.listdir(cwd):
    if tif.lower().endswith('.tif'):
        images.append(tif)

plt.figure(1)
count=1

for i in images:
    image = plt.imread(i)
    plt.subplot(2, 5, count)
    plt.imshow(image, cmap='gray')
    count=count+1

plt.show()'''