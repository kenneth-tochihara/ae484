import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd
        
# Problem 1 Code
def problem1(filename1,filename2,filename3,filename4,filename5):
    file1 = pd.read_csv(filename1)
    file2 = pd.read_csv(filename2)
    
    # initialize figure properties
    plt.figure()
    plt.rcParams.update({"font.family" : "Times", "mathtext.fontset" : "stix", "text.usetex": True})
    plt.rcParams.update({'font.size': 14})
    plt.rcParams['axes.axisbelow'] = True
    plt.rcParams['lines.markersize'] = 5
    fig = plt.figure(dpi = 500, figsize=[7, 5])
    plt.xlabel(r"Angle of Attack"); plt.ylabel(r"Coefficient of Lift")
    
    #plots
    plt.plot(file1.iloc[:,0],file1.iloc[:,1],label = 'NACA 0012', color = "dodgerblue", linewidth = 3)
    plt.plot(file2.iloc[:,0],file2.iloc[:,1],label = 'NACA 4412', color = "red",  linewidth = 3)
    
    # final formatting before saving
    plt.grid(); plt.legend(); plt.tight_layout()
    fig.savefig(filename3); fig.clear()
    
    # initialize figure properties
    plt.figure()
    plt.rcParams.update({"font.family" : "Times", "mathtext.fontset" : "stix", "text.usetex": True})
    plt.rcParams.update({'font.size': 14})
    plt.rcParams['axes.axisbelow'] = True
    plt.rcParams['lines.markersize'] = 5
    fig2 = plt.figure(dpi = 500, figsize=[7, 5])
    plt.xlabel(r"Angle of Attack"); plt.ylabel(r"Coefficient of Drag")
    
    #plots
    plt.plot(file1.iloc[:,0],file1.iloc[:,2],label = 'NACA 0012', color = "dodgerblue", linewidth = 3)
    plt.plot(file2.iloc[:,0],file2.iloc[:,2],label = 'NACA 4412', color = "red",  linewidth = 3)
    
    # final formatting before saving
    plt.grid(); plt.legend(); plt.tight_layout()
    fig2.savefig(filename4); fig2.clear()
    
    # initialize figure properties
    plt.figure()
    plt.rcParams.update({"font.family" : "Times", "mathtext.fontset" : "stix", "text.usetex": True})
    plt.rcParams.update({'font.size': 14})
    plt.rcParams['axes.axisbelow'] = True
    plt.rcParams['lines.markersize'] = 5
    fig3 = plt.figure(dpi = 500, figsize=[7, 5])
    plt.xlabel(r"Coefficient of Lift"); plt.ylabel(r"Coefficient of Drag")
    
    #plots
    plt.plot(file1.iloc[:,1],file1.iloc[:,2],label = 'NACA 0012', color = "dodgerblue", linewidth = 3)
    plt.plot(file2.iloc[:,1],file2.iloc[:,2],label = 'NACA 4412', color = "red",  linewidth = 3)
    
    # final formatting before saving
    plt.grid(); plt.legend(); plt.tight_layout()
    fig3.savefig(filename5); fig3.clear()

# Problem 2 Code        
def problem2(filename1,filename2):
    pass

# Problem 3 Code
def problem3(filename1,filename2):
    file1 = pd.read_csv(filename1)
    
    # initialize figure properties
    plt.figure()
    plt.rcParams.update({"font.family" : "Times", "mathtext.fontset" : "stix", "text.usetex": True})
    plt.rcParams.update({'font.size': 14})
    plt.rcParams['axes.axisbelow'] = True
    plt.rcParams['lines.markersize'] = 5
    fig = plt.figure(dpi = 500, figsize=[7, 5])
    plt.xlabel(r"Angle of Attack"); plt.ylabel(r"Coefficient of Moment")
    
    #plots
    plt.plot(file1.iloc[:,0],file1.iloc[:,8],label = 'NACA 0012', color = "dodgerblue", linewidth = 3)
    
    # final formatting before saving
    plt.grid(); plt.legend(); plt.tight_layout()
    fig.savefig(filename2); fig.clear()
    
    
# run all problems
def main():
    problem1('homeworks/homework3/george/data/NACA0012_1.csv','homeworks/homework3/george/data/NACA4412_1.csv','homeworks/homework3/george/plots/problem1_a.png','homeworks/homework3/george/plots/problem1_b.png','homeworks/homework3/george/plots/problem1_c.png')
    problem3('homeworks/homework3/george/data/NACA0012_3_finite.csv','homeworks/homework3/george/plots/problem3_ai.png')
if __name__ == "__main__":
    main()
    