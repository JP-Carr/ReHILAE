from scipy.optimize import curve_fit
import numpy as np
import pylab
import matplotlib.pyplot as plt
import math
import matplotlib

def Function(x,a1,a2,a3):
	return a1*x**2.+a2*x+a3

xs = [2.2,2.5,2.8,3.0,3.2, 3.3, 3.7, 4.1, 4.6, 4.8, 5.1, 5.3, 5.8 ]
y = np.array([0.52, 0.74, 0.77, 0.88, 0.84, 0.85, 1.01, 0.87, 1.19, 1.12, 1.27, 1.08, 1.10]) # data from SC4K Sobral 
ys = np.array([math.log10(i*10**40) for i in y])
ys_err = [0.05,0.075,0.095,0.095,0.09,0.095,0.18,0.13,0.35,0.32,0.4,0.185,0.185]
p2 = pylab.polyfit(xs, ys, 2.0)
p = pylab.poly1d(p2)
params = p.coefficients

pfit, pcov = curve_fit(Function, xs,ys,p0=params,sigma=ys_err)

error = []
for i in range(len(pfit)):
  try:
    error.append(np.absolute(pcov[i][i])**0.5)
  except:
    error.append(0.00)
BFP = pfit
err_BFP = np.array(error)

print ('log(P_Lya): y = (%s+-%s)x^2  + (%s+-%s)x + (%s-%s)' %(round(BFP[0],5),round(err_BFP[0],5),round(BFP[1],5),round(err_BFP[1],5),round(BFP[2],5),round(err_BFP[2],5)))

a1, a2, a3 = BFP[0], BFP[1], BFP[2]
a1_err, a2_err,  a3_err = err_BFP[0], err_BFP[1], err_BFP[2]
zs = list(np.linspace(0.0051,20,10000))
scipy_fit = [Function(z,a1,a2,a3) for z in zs]
n = 1000
a1_list = np.random.normal(a1, a1_err*0.2, n)
a2_list = np.random.normal(a2, a2_err*0.2, n)
a3_list = np.random.normal(a3, a3_err*0.2, n)

all_runs = []
for _ in a1_list:
    all_runs.append([])

for A,B,C,loop in zip(a1_list,a2_list,a3_list,all_runs):
    for z in zs:
        parameter = np.random.randint(3)
        if parameter == 0:
            loop.append(Function(z,A,a2,a3))
        elif parameter == 1:
            loop.append(Function(z,a1,B,a3))
        else:
            loop.append(Function(z,a1,a2,C))


median, median_upper_percentile, median_lower_percentile = [],[],[]
for z in zs:
    ind = zs.index(z)
    P_Lya = [i[ind] for i in all_runs]
    median_lower_percentile.append(np.percentile(P_Lya,16))
    median.append(np.median(P_Lya))
    median_upper_percentile.append(np.percentile(P_Lya,84))


plt.figure('Lya_Quad')
#plt.plot(zs,scipy_fit,color='black',label='SciPy fit')
plt.fill_between(zs,  median_lower_percentile, median_upper_percentile, alpha=0.4, color = "grey", edgecolor = "black", linewidth = 1.2, label=r'$1\sigma$ conf. interval')
plt.plot(zs, median, label='ReHiLAE (this study, median)',color='black')
plt.scatter(xs,ys,color='black',marker='.',label='Sobral+2018')
plt.errorbar(xs,ys,yerr=ys_err,color='black',ls='none')
plt.legend()
plt.xlim(0,20)
plt.xlabel(r'Redshift (z)')
plt.ylabel(r'$log_{10}(\rho_{Ly\alpha} \ [erg \ s^{-1} \ Mpc^{-3}])$')
plt.tick_params(which='both',direction='in',right=True,top=True)
plt.legend()
matplotlib.rcParams['lines.linewidth'] = 6
matplotlib.rcParams['axes.linewidth'] = 2.0
matplotlib.rcParams['xtick.major.size'] = 9
matplotlib.rcParams['xtick.minor.size'] = 5
matplotlib.rcParams['xtick.major.width'] = 1.9
matplotlib.rcParams['xtick.minor.width'] = 1.3
matplotlib.rcParams['ytick.major.size'] = 9
matplotlib.rcParams['ytick.minor.size'] = 4
matplotlib.rcParams['ytick.major.width'] = 1.9
matplotlib.rcParams['ytick.minor.width'] = 1.3

plt.show()