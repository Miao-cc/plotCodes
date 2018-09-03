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




if (len(sys.argv)<1):
  print 'too few inputs!'
  sys.exit()
else:
  print 'input seems OK'



print 'record start time:'
starttime=datetime.datetime.now()
print starttime


rowdatafile=sys.argv[1]
filename = rowdatafile



nsblk=4096
nchan=4096


data1 = np.fromfile(rowdatafile,dtype=np.float32,count=-1).reshape((64,nsblk,1,nchan,1),order='C')
a,b,c,d,e = data1.shape
if c > 1:
    data = data1[:,:,0,:,:].squeeze().reshape((-1,d))
else:
    data = data1.squeeze().reshape((-1,d))
l, m = data.shape
data = data.reshape(l/64, 64, d).sum(axis=1)
print data.shape
#data -= data.mean(axis=0).transpose().astype(np.uint64)

from pylab import *
xlabel('time(sec)')
ylabel('freq(MHz)')
tsamp = 0.0002
df = 0.25
xticklabel=[]
strxticklabel=[]
for i in range(32): 
    xticklabel.append(i*64*2)
    strxticklabel.append(str(int(i*4096*tsamp*2)))
yticklabel=[]
stryticklabel=[]
for i in range(25): 
    yticklabel.append(i*200)
    stryticklabel.append(str(i*df*200))

yticks(yticklabel,stryticklabel)
xticks(xticklabel,strxticklabel)
title('filename: %s' %filename.split('/')[-1])
imshow(data.T, aspect='auto')
colorbar()
#plot(data.sum(axis=0))
#plot(data.sum(axis=1))
show()
#rowdata=np.fromfile(rowdatafile,dtype=np.float32,count=-1)

#print "rowdata.shape:",rowdata.shape
#print "simdata.shape",simdata.shape
#print "simdata.shape",simdata[0,0,0,:,0].shape

#temp=np.zeros(64*nsblk)
#
#print "start reshape file",datetime.datetime.now()
#simdata = np.fromfile(rowdatafile,dtype=np.float32,count=-1).reshape((64,nsblk,1,nchan,1),order='C')
#print "end reshape file",datetime.datetime.now()
#
##simdata = simdata.reshape(nchan, 64*nsblk).T.reshape((64, nsblk, nchan))
#simdata = simdata.reshape((64, nsblk, nchan))
#
##for i in range(64):
#    ##temp[i*4096:(i+1)*4096]=simdata[i,:,0,1000,0]
#    #temp[i*4096:(i+1)*4096]=simdata[i,:,1000]
#
#temp = simdata[:,:,1000].flatten()
##temp = simdata[1,:,0,1000,0]
#
#print np.max(temp)
#plot(temp)
#show()
#
#plot(np.abs(np.fft.rfft(temp)))
#show()
#
#
##temp1=np.zeros(64*nsblk)
##print "start reshape file",datetime.datetime.now()
##simdata=np.zeros((64,nsblk,1,nchan,1))
##
##rowdata=np.fromfile(rowdatafile,dtype=np.float32,count=-1)
##
##print "rowdata.shape:",rowdata.shape
##print "simdata.shape",simdata.shape
##print "simdata.shape",simdata[0,0,0,:,0].shape
##for i in range(64):
##    for j in range(nsblk):
##        simdata[i,j,0,:,0]=rowdata[(i*4096+j)*nchan:(i*4096+j+1)*nchan]
##
##print "end reshape file",datetime.datetime.now()
##
##
##for i in range(64*nsblk):
##    temp1[i]=rowdata[i*nchan+1000]-temp[i]
###
###
##plot(temp1)
####plot(data.sum(axis=0))
####plot(data.sum(axis=1))
##show()
#
#
