import numpy as np 
import fitsio
import os
import datetime
import time
import sys
from array import array
from pylab import *
import astropy.io.fits as pyfits
from scipy import interpolate
import astropy.io.fits as pyfits
from decimal import Decimal


print 'record start time:'
starttime=datetime.datetime.now()
print starttime

filename=sys.argv[1]

nsblk=4096
nchan=4096


print "start reshape file",datetime.datetime.now()
simdata = np.fromfile(filename,dtype=np.float32,count=-1).reshape((64,nsblk,1,nchan,1),order='C')

print "end reshape file",datetime.datetime.now()
print "shape of simdata: ", simdata.shape

from pylab import *
from matplotlib.ticker import  MultipleLocator

switch_backend('ps')
#a,b,c,d,e = simdata.shape
#fig = figure(figsize=(16,12*c), dpi=1000)
fig = figure(figsize=(16,12), dpi=1000)


data = simdata[:,:,0,3000,0].reshape(64*4096)

print "shape of simdata: ", data.shape
#data -= data.mean(axis=0).transpose().astype(np.uint64)
ax=fig.add_subplot(111)
#ax.imshow(data.T, aspect='auto')
ax.plot(range(len(data)),data)
#ax.set_ylabel('num of channel  '+'pol'+str(i+1))
#ax.set_xlim(0.,tsamp*nsamp)
title(filename.split('/')[-1])

#ax.set_ylabel('bandpass of '+'pol'+str(i+1))
#ax.set_xlim(0.,obsnchan)
#colorbar()
#plot(data.sum(axis=0))
#plot(data.sum(axis=1))
#show()



#for i in range(c):
#    #data = simdata[:,:,i,0,:].squeeze().reshape((-1,d))
#    data = simdata[:,:,i,1000,:].squeeze().reshape((-1,d))
#    l, m = data.shape
#
#    #data = data.reshape(l/64, 64, d).sum(axis=1)
#    bandpass = np.sum(data,axis=0)
#    print data.shape
#    #data -= data.mean(axis=0).transpose().astype(np.uint64)
#    subplotnum=int(str(2*c)+'1'+str(2*i+1))
#    ax=fig.add_subplot(subplotnum)
#    ax.imshow(data.T, aspect='auto')
#    ax.set_ylabel('num of channel  '+'pol'+str(i+1))
#    #ax.set_xlim(0.,tsamp*nsamp)
#    if i < 1 : title(filename.split('/')[-1])
#    
#    subplotnum=int(str(2*c)+'1'+str(2*i+2))
#    ax=fig.add_subplot(subplotnum)
#    ax.plot(bandpass)
#    ax.set_ylabel('bandpass of '+'pol'+str(i+1))
#    #ax.set_xlim(0.,obsnchan)
#    #colorbar()
#    #plot(data.sum(axis=0))
#    #plot(data.sum(axis=1))
#    #show()
xlabel('time (s)')
imgfilename=(filename.split('/')[-1])[:-5]+'.png'
print "img file name", imgfilename
savefig(imgfilename)
clf()
