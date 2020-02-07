import matplotlib.pyplot as plt
import numpy as np
import MPhys_model as mod
import math
from Redshift import redshift as z
import plotter

#TIME VALUES
startTime = mod.startTime
finishTime = mod.finishTime
timeStep = mod.timeStep

#GENERATE Z, Z_alt, AND t ARRAYS
Z,t = z(startTime, finishTime, timeStep)
Z_alt,t = z(startTime, finishTime, timeStep, True)
"""
#PLOT t AGAINST Z
plt.plot(t,Z, color='red', label='Cosmology Equation')
plt.plot(t,Z_alt, color='blue', label='Approximation')
plt.xlabel('Cosmic Time [Gyrs]')
plt.ylabel('Redshift')
plt.legend()
plt.show()
"""

plotter.multiplot([t,t], [Z,Z_alt], "", 'Cosmic Time [Gyrs]', "Redshift",['Cosmology Equation','Approximation'])





#Connor's code
"""
This file will verify the cosmic time - redshift equation shown in https://arxiv.org/pdf/gr-qc/0506079.pdf 
by comparing it to the original equation in our in model

import math
import numpy as np
import matplotlib.pyplot as plt

def cosmoEq(t):
    W_M=0.308 #matter energy density parameter
    W_lambda=0.692 #dark energy density parameter
    H_0=0.0692 #Gyr⁻¹ - Hubble's constant
    return (((math.sinh(3*W_lambda**0.5*t / (2*1/H_0) ) * (W_lambda/W_M)**-0.5)**(-2/3)) -1)

def approx(t):
    return (((28./(t))-1.)**(1./2.)-1.)

ts = np.linspace(0.051,14,1000000) # time in Gyr
x = [cosmoEq(i) for i in ts]
y = [approx(i) for i in ts]

plt.plot(ts,x, color='red', label='Cosmology Equation')
plt.plot(ts,y, color='blue', label='Approximation')
plt.xlabel('Cosmic Time [Gyrs]')
plt.ylabel('Redshift')
plt.legend()
plt.show()
"""