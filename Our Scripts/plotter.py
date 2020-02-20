"""
Provides functions to produce graphs with single and multiple plots
"""
import matplotlib.pyplot as plt
import ErrorFits
#import numpy as np
#import MPhys_model.py as mod

#path=None

#PLOTS PARTICLE POSITION AS STATIC GRAPH
def plot(x,y,title,x_lab,y_lab,path=None,error_list):
    #Outputs or saves a single Cartesian plot from 2 arrays
    plt.figure(figsize=(7,7))
    """
    plt.ylim(bottom=0)
    plt.ylim(top=max(y))
    """
    plt.xlim(left=0)
    plt.xlim(right=max(x)*1.1)
    plt.title(title)
    plt.xlabel(x_lab)
    plt.ylabel(y_lab)
    plt.plot(x,y)
    
    min_list, max_list = ErrorFits.error_Range(x,y,error_list[1],error_list[2])
    plt.fill_between(x,min_list,max_list,lw=1,color='#0066ff',alpha=0.1,zorder = 90)
  
    if path==None:
        plt.show()
    else:
        plt.savefig("plots\\"+path+"\\"+title+".png")
    

def multiplot(x_list,y_list,title,x_lab,y_lab,legend_list=None,path=None):
    #Outputs or saves a multiple plots on a single Cartesian axis from 2 nested arrays
    max_x=max([max(i) for i in x_list])
    
    plt.figure(figsize=(7,7))
    plt.xlim(left=0)
    plt.xlim(right=max_x*1.1)
    plt.title(title)
    plt.xlabel(x_lab)
    plt.ylabel(y_lab)
    for i in range(len(x_list)):
        plt.plot(x_list[i], y_list[i])
    if legend_list != None:
        plt.legend(legend_list)
        
    if path==None:
        plt.show()
    else:
        plt.savefig("plots\\"+path+"\\"+title+".png")
    return