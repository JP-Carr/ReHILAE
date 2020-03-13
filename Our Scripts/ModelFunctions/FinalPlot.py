import matplotlib.pyplot as plt
import numpy as np
import math
import random_array_generator as rag
import pandas as pd
import LAE_with_errors as main

ts = np.linspace(0.051,14,100000) # time in Gyr
zs= ((((28./(ts))-1.)**(1./2.)-1.)) # conversion from Gyr to redshift

C1 = [0.0013679194302549992]
C1_error = [0.0009034769902604823]

C2 = [-0.05592731916980156]
C2_error = [0.024847250273459104]

C3 = [0.29377928649363305]
C3_error = [0.21010382042922288]

C4 = [26.095271603086044]
C4_error = [0.5405447975405038]

P1 = [1.0388337446404217]
P1_error = [0.14499428119168625]

P2 = [39.2529986910512]
P2_error = [0.09253769652436827]


C1_P_UV = rag.random_Arrays(len(C1),C1,C1_error,C1_error)
C2_P_UV = rag.random_Arrays(len(C2),C2,C2_error,C2_error)
C3_P_UV = rag.random_Arrays(len(C3),C3,C3_error,C3_error)
C4_P_UV = rag.random_Arrays(len(C4),C4,C4_error,C4_error)
P1_P_Lya = rag.random_Arrays(len(P1),P1,P1_error,P1_error)
P2_P_Lya = rag.random_Arrays(len(P2),P2,P2_error,P2_error)

rawData = []
for i,j,k,l,m,n in zip(C1_P_UV, C2_P_UV, C3_P_UV, C4_P_UV, P1_P_Lya, P2_P_Lya):
    arguements = (i[0], j[0], k[0], l[0], m[0], n[0])
    rawData.append((main.main(ts,arguements)))

data=[]
for result in rawData:
    anonmalies = result[:1000:]
    if all([q[0]<1. for q in anonmalies]):
        data.append(result)

print(len(rawData))
print(len(data))

plt.figure()
for result in data:
    plt.plot(zs,result)
plt.xlabel("Redshift (z)")
plt.ylabel("Fractions of Ionised Hydrogen")

plt.figure('Ionised_Hydrogen_UV  10000')
plt.title("Fraction of ionised H with respect to redshift")

median, median_lower_percentile, median_upper_percentile = rag.median_y_values(len(data[0]),data)
plt.xlabel("Redshift (z)")
plt.ylabel("Fractions of Ionised Hydrogen")
plt.plot(zs,median, color = "black", label="LAE")

plt.fill_between(zs,  median_lower_percentile, median_upper_percentile, alpha=0.4, color = "steelblue", edgecolor = "black", linewidth = 1.2)
plt.fill_betweenx(median,6,10, color = "lightgrey", alpha = 0.3, edgecolor = "black", linewidth = 5)

plt.show()