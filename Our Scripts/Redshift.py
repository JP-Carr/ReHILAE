import matplotlib as plt
import numpy as np
import MPhys_model as mod
import plotter
import math

#TIME VALUES
startTime=0.01
finishTime=14
timeStep=0.01

# FUNCTION TO GENERATE Z AND T ARRAYS
def redshift(startTime, finishTime, timeStep, alt = False): 
    
    #global t
    t = np.arange(startTime, finishTime, timeStep)
    Z = []
    
    for i in t:
        Z.append(mod.z(i, alt))
    
    return Z,t


#QUICK PLOT
    """
Z = redshift(startTime, finishTime, timeStep)
plotter.plot(t,Z,"A plot of redshift against time","z","t")
"""