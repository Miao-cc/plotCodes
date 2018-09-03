import numpy as np
import math
import matplotlib.pyplot as plt

#plot for width
#width
#width = np.fabs(2*dt_dm[j]*chanbw/(chanfref[j])) + head->width;
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

meanFref = 500
randomNum = 0.5

period = 3
tsamp = 0.0002
#phaseNum = 4* int(period / tsamp)
phaseNum = int(period / tsamp)
#width = 0.05
width = pulseWidth(period, meanFref,randomNum)*period
#width = pulseWidth(period, meanFref,randomNum)
count = 0
#1/width/width > 100
#exp(-pow(phase,2)/2.0/width/width)/width/sqrt(2.* 3.14159265) * randarr[phasenum]* exp(gasdev(&idum)) / e;
profile = np.zeros(phaseNum)
for i in range(phaseNum):
    tval = i*tsamp 
    phase = tval/period % 1.
    if (phase < 0.) : phase += 1.
    phase -= 0.5;
    
    #phasenum = (int)(tval/head->p0-fmod(tval/head->p0, 1.));
    if 1/width/width > 100:
        profile[i] = math.exp(-pow(phase,2)/2.0/width/width)/width/np.sqrt(2.* math.pi) #* randarr[phasenum]* exp(gasdev(&idum)) / e
    else:
        profile[i] = math.exp((1/width/width) * math.cos(phase))/2./math.pi/np.i0((1/width/width)) # * randarr[phasenum] * exp(gasdev(&idum)) / e;

for i in range(phaseNum):
    if profile[i] >= max(profile)*0.7:
        count += 1
    #profile[i] = math.exp((1/width/width) * math.cos(phase))/2./math.pi/np.i0((1/width/width)) # * randarr[phasenum] * exp(gasdev(&idum)) / e;
print sum(profile)*1./phaseNum
profile = profile *0.001/ (sum(profile)*1./phaseNum)
print count,len(profile),count*1./float(len(profile))
print int(period / tsamp)
print 'width: %s' % (np.size(np.where(profile > 0.00001))/(phaseNum*1.))
print 'num of profile > 0: %s' %(np.size(np.where(profile > 0.00001)))
print 'width: %s, phaseNum: %s' %(width, phaseNum)
plt.plot(profile)
#plt.scatter(np.arange(len(profile)),profile)
plt.xlabel('phaseNum')
plt.ylabel('Flux')
plt.text(17900,0.007,'width 0.05 \nflux : 0.001 \nperiod: 1 sec \ntsamp: 0.0002 sec')
plt.title('sample of pulse profile1')

plt.show()

#1/width/width > 100
#exp(kappa * cos(phase))/2./3.14159265/bessi0(kappa) * randarr[phasenum] * exp(gasdev(&idum)) / e;
#profile[i] = math.exp((1/width/width) * math.cos(phase))/2./math.pi/np.i0(kappa) # * randarr[phasenum] * exp(gasdev(&idum)) / e;


