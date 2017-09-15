##Depth Analysis Version 2.0 plot Walk Data---> Stride length, Stride time, gait Speed
##get Centroid Data
##Code By - Anup Mishra
##Update 03/14/2017

import sys
import pandas as ps
import math as m
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import csv
from numpy import linspace, loadtxt, ones, convolve, NaN, Inf, arange, isscalar, asarray, array

##Get and set the centroid data
#path=r"D:\EMBC Data 2016-Ben\Walk data\Test"
#CentroidData=ps.read_csv(r"D:\EMBC Data 2016-Ben\Walk data\Test\CentroidData.csv")

path= ps.read_csv(r"~\Documents\PT_Data_Collection\PathToCurrentDepthFolder.csv")
CentroidData=ps.read_csv(path.ix[0,1]+"\\CentroidData.csv")
centroids = CentroidData;
centroids.columns = ['min', 'sec', 'milis', 'x','y','z']
centroids['z']=centroids['z']*-1
centroids=centroids[['x','y','z']]

#plt.plot(centroids['z'], centroids['x'])
#plt.show()

##Get the time series time data
time=[]
for i in range(len(centroids['x'])):
    time.append((CentroidData.ix[i,'min'])*60+(CentroidData.ix[i,'sec'])+CentroidData.ix[i,'milis']*0.001)
    
time= time-time[1]

F=[]
for i in range(len(centroids['x'])):
    string=path.ix[0,1]
    string+="\\"+str(i+1)+".csv"
    F.append(ps.read_csv(string))
	
corr=[]
for i in range(0, len(centroids['x']), 1):
    ##Convert to inches
    steps =F[i]*39.3701;
    steps.columns=['x','y','z']
    steps['z']= steps['z']*-1
    
    ##Find Mean of data
    steps['x']=steps['x']-steps['x'].mean()
    steps['z']=steps['z']-steps['z'].mean()
    Foot = steps[['x','z']]

    
    newArray = ps.DataFrame([[0, 0]], columns=list('xz'))
    counter=0;

    
    newArray= Foot.loc[abs(Foot['x'])<25,:]
                
    newArray['x']=newArray['x']-newArray['x'].mean()
    newArray['z']=newArray['z']-newArray['z'].mean()

    ##Find correlation
    M = newArray['x']*newArray['z']
    corr.append(sum(M)/len(newArray))   
	
##Moving Mean
def movingaverage(interval, window_size):
    window = np.ones(int(window_size))/float(window_size)
    return np.convolve(interval, window, 'same')
	
##Check Corr data and do moving mean
corr_av= movingaverage(corr, 15)
corr_av= movingaverage(corr_av, 5)
#plt.plot(corr,'r--',corr_av,'g^')
#plt.show()

#Peak detect
def peakdet(v, delta, x = None):
    """
    Converted from MATLAB script at http://billauer.co.il/peakdet.html
    
    Returns two arrays
    
    function [maxtab, mintab]=peakdet(v, delta, x)
    %PEAKDET Detect peaks in a vector
    %        [MAXTAB, MINTAB] = PEAKDET(V, DELTA) finds the local
    %        maxima and minima ("peaks") in the vector V.
    %        MAXTAB and MINTAB consists of two columns. Column 1
    %        contains indices in V, and column 2 the found values.
    %      
    %        With [MAXTAB, MINTAB] = PEAKDET(V, DELTA, X) the indices
    %        in MAXTAB and MINTAB are replaced with the corresponding
    %        X-values.
    %
    %        A point is considered a maximum peak if it has the maximal
    %        value, and was preceded (to the left) by a value lower by
    %        DELTA.
    
    % Eli Billauer, 3.4.05 (Explicitly not copyrighted).
    % This function is released to the public domain; Any use is allowed.
    
    """
    maxtab = []
    mintab = []
       
    if x is None:
        x = arange(len(v))
    
    v = asarray(v)
    
    if len(v) != len(x):
        sys.exit('Input vectors v and x must have same length')
    
    if not isscalar(delta):
        sys.exit('Input argument delta must be a scalar')
    
    if delta <= 0:
        sys.exit('Input argument delta must be positive')
    
    mn, mx = Inf, -Inf
    mnpos, mxpos = NaN, NaN
    
    lookformax = True
    
    for i in arange(len(v)):
        this = v[i]
        if this > mx:
            mx = this
            mxpos = x[i]
        if this < mn:
            mn = this
            mnpos = x[i]
        
        if lookformax:
            if this < mx-delta:
                maxtab.append((mxpos, mx))
                mn = this
                mnpos = x[i]
                lookformax = False
        else:
            if this > mn+delta:
                mintab.append((mnpos, mn))
                mx = this
                mxpos = x[i]
                lookformax = True

    return array(maxtab), array(mintab)

maxtab_wt, mintab_wt = peakdet(corr_av,1)
plt.plot(corr_av)
plt.scatter(array(maxtab_wt)[:,0], array(maxtab_wt)[:,1], color='blue')
plt.scatter(array(mintab_wt)[:,0], array(mintab_wt)[:,1], color='red')
#plt.show()

#Start end frames for time
if(maxtab_wt[0][0]<mintab_wt[0][0]):
    time_start=maxtab_wt[0][0];
else:
    time_start=mintab_wt[0][0];
    
if(maxtab_wt[len(maxtab_wt)-1][0]>mintab_wt[len(mintab_wt)-1][0]):
    time_end=maxtab_wt[len(maxtab_wt)-1][0];
else:
    time_end=mintab_wt[len(mintab_wt)-1][0];    

time_walk= time[time_start:time_end];

timeOfCompletion = time_walk[len(time_walk)-1]-time_walk[0]
numberOfSteps = len(maxtab_wt)+len(mintab_wt)
gait_speed = 4/timeOfCompletion
avg_step_length = 4/numberOfSteps
cadance = numberOfSteps/4

#centroid_smooth=centroids;
#centroid_smooth['x']= movingaverage(centroids['x'], 25)
#centroid_smooth['z']= movingaverage(centroids['z'], 25)
#centroid_smooth = centroid_smooth.loc[time_start:time_end-1,:];
#plt.plot(centroid_smooth['z'], centroid_smooth['x'])
#plt.show()
#centroid_smooth=centroid_smooth[['z','x']]
#dist=0
#for i in range(1, len(centroid_smooth)-1, 1):
#dist=np.linalg.norm(centroid_smooth.iloc[1]-centroid_smooth.iloc[len(centroid_smooth)-1])

timeOfCompletion
numberOfSteps
gait_speed
avg_step_length
cadance

#output
with open('FourMWalkResultsPython.csv', 'w') as csvfile:
    fieldnames = ['timeOfCompletion(s)', 'numberOfSteps','gait_speed(m/s)','avg_step_length(m)','cadance']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({ 'timeOfCompletion(s)': timeOfCompletion, 'numberOfSteps':numberOfSteps, 'gait_speed(m/s)': gait_speed, 'avg_step_length(m)':avg_step_length, 'cadance':cadance})

