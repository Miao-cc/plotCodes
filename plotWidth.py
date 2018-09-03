import numpy as np
import math
import os, sys, glob, re
from commands import getoutput
import time
import datetime

def pulseWidth(period,meanFref,randomNum):
    meanFref = meanFref/1000.
    B=1.*1E12
    R_LightCylinder = 4.77*10000.*period
    periodDot = ((B/(3.2*1E19))**2)/period
    R_EmisionBeam = 400.*pow(meanFref,-0.26)*pow((periodDot*(1E15)),0.07)*pow(period,0.3)
    rho = 86.*pow(R_EmisionBeam/R_LightCylinder,0.5)
    rho = rho/360.
    w = 2*rho*pow((1.-randomNum**2),0.5)
    return w

periodNum = 10000
period = [(i+1)*0.001 for i in range(periodNum)]
width = []
meanFref = 500
randomNum = 0.5
imgfilename = 'pulseWidth.png'

for p in period:
    width.append(pulseWidth(p,meanFref,randomNum))

from pylab import *
from matplotlib.ticker import  MultipleLocator

switch_backend('ps')
##a,b,c,d,e = simdata.shape
##fig = figure(figsize=(16,12*c), dpi=1000)
fig = figure(figsize=(16,12), dpi=1000)
#plot(period, width)
semilogx(period, width)
yticks(np.arange(min(width), max(width), 0.05))
grid(True)
xlabel(r'$\log_{10}$'+' Period (sec)')
ylabel('width')
title('pulse width')


#xlabel('time (s)')
imgfilename = 'pulseWidth.png'
print "img file name", imgfilename
savefig(imgfilename)
clf()
