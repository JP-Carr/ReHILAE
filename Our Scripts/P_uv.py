import matplotlib as plt
import numpy as np
import MPhys_model as mod
import plotter
import math
from Redshift import redshift as z

startTime=0.01
finishTime=14
timeStep = 0.01

Z,t = z(startTime, finishTime, timeStep)
#print (z)
P_uv=[mod.P_uv(i) for i in Z]
#print (t_rec)

plotter.plot(Z,P_uv,"A plot of redshift against UV density","z","log(P_uv)")