# -*- coding: utf-8 -*-
"""
@author: Matrucious
"""

# Graph producer

import numpy as np
from matplotlib import pyplot as plt

print("This program takes input of a polar coordinate\n"+
      "and graphs it in either polar, or cartesian form\n")

#Produce theta variable
theta = np.arange(0, 2*np.pi, .001)[1:]

#Input polar equation HERE!
#Example: 2*np.sin(theta)
r=0

print("Getting ready to plot curve..\n"+
      "Do you wish to convert to cartesion?\n"+
      "Y/N")
ans=input()

#Test to use cartesian or not
if ans == "Y" or ans == "y":
    #Make cartesian plot figure
    fig = plt.figure(figsize = (5, 5))
    
    #Convert to cartestian
    x = r*np.cos(theta)
    y = r*np.sin(theta)
    
    #Add sub-plot and plot functions of x,y
    ax = fig.add_subplot(polar = False)
    ax.plot(x, y)
    
    plt.show()

else:
    #Make plt figure
    fig = plt.figure()

    #Make sub-plot with attribute "polar"
    ax = fig.add_subplot(polar=True)
    
    #Change negative r values to positive, rotating theta by 180º
    theta = np.where(r >= 0, theta, theta + np.pi)
    r = np.abs(r)
    
    #Plot function
    ax.plot(theta, r)
    
    #Show plot
    plt.show()
      
      #hello
