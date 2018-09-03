# -*- coding: utf-8 -*-
import numpy as np
import math
import matplotlib.pyplot as plt
import glob
from pylab import *
from matplotlib.ticker import  MultipleLocator


path = '/public/home/mcc/psrsoft/plotforPPT/data/simdata'
#path = '/public/home/mcc/work/test-1000file2/result/foldfile'
filelist = glob.glob(path+'/*.bestprof')
#print filelist
#filelist = ['/public/home/mcc/work/test-1000file2/result/foldfile/test10_DM_63.1_Flux_0.006310_P0_0.10000s_cut_100.00ms_Cand.pfd.bestprof']

#switch_backend('ps')
count = 0
for i in filelist:
    count += 1
    print i,count
    f = open(i,'r')
    lines = f.readlines()
    f.close()
    #print float(lines[28].split()[1])
    profile = []
    for j in range(len(lines)-27):
        j += 27
        profile.append(float(lines[j].split()[1]))

    maxProfile = max(profile)
    print  min(profile), max(profile)
    #while (profile)
    #width = maxProfile/maxProfile
    





    profile = profile * 2
    #plt.scatter(np.arange((len(lines)-27)),profile)
    fig = figure(figsize=(16,12), dpi=80)
    plt.title('%s' %i.split('/')[-1])
    plt.plot(profile)
    plt.scatter(np.arange(len(profile)),profile)
    plt.show()
    #nextloop = raw_input('Please enter:')
    #if (nextloop != ' '): continue

