#!/usr/bin/env python
# coding: utf-8

# In[72]:


import csv
import sys
import math
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.patches import ConnectionPatch
import numpy as np

class project(object):
    def API(self, values):
        self.ReadFile(values)
        self.createCPC(values)
        
    def ReadFile(self, values):                         #Reads values into 2d array
        with open('input.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            count = 0
            for line in csv_reader:
                values.append([])
                line=list(line)
                for i in line:
                    values[count].append(i)
                count = count + 1

    def createCPC(self,values):
        xCoords =[]
        yCoords =[]
        totalX = 0
        totalY = 0
        currentClass = 1
        xLength = len(values)        # Rows
        fig = plt.figure(figsize=(7,7))                            #Creating the sub plost and plot points
        fig.subplots_adjust(hspace=1) 
        for i in range(1, (xLength - 1)):       # 1- 6
            yLength = len(values[i])        # Columns
            for j in range(1, (yLength - 1)):
                if (int(values[i][yLength - 1]) == currentClass):
                    if ((len(xCoords)) <= (len(yCoords))):           #X-values for graph
                        totalX = float(values[i][j]) + float(totalX)    #Total  distance x
                        xCoords.append(float(totalX))
                    else:                                                             #Y-values for graph
                        totalY = float(values[i][j]) + float(totalY)    #Total  distance y  
                        yCoords.append(float(totalY)) 
                else:                 
                    n = len(fig.axes)                                           # Adjust the number of graphs in figure
                    for b in range(n):
                        fig.axes[b].change_geometry(n+1, 1, b+1)
                    ax = fig.add_subplot(n+1, 1, n+1)
        	    ax.set_xlabel('x')
        	    ax.set_ylabel('y')
                    ax.set_title("CPC for Class: " + str(currentClass))          # Create the graph for each class
                    ax.plot(xCoords, yCoords,'--bo')
                    print("Class: ", currentClass , " CPC values...")                #Printing for our use/ Display on the screen
                    for m in range(len(xCoords)):
                        print("(" + str(xCoords[m]) + "," + str(yCoords[m]) +")")
                    xCoords.clear()                               # Reset everything for next class
                    yCoords.clear()
                    totalX = 0
                    totalY = 0
                    currentClass = currentClass +1
                    xCoords.append(float(values[i][j]))     # Append the first X-coord of class

        print("Class: ", currentClass , " CPC values...")                # Printing the values of CPC plots
        for m in range(len(xCoords)):
            print("(" + str(xCoords[m]) + "," + str(yCoords[m]) +")")
        n = len(fig.axes)
        for b in range(n):
            fig.axes[b].change_geometry(n+1, 1, b+1)
        ax = fig.add_subplot(n+1, 1, n+1)                                     # Creating one last graph to account for the last class (wasn't included in for loop)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title("CPC for Class: " + str(currentClass))
        ax.plot(xCoords, yCoords,'--bo')
        plt.show()
                    
    def main():
        values = [[]]
        obj = project()
        obj.API(values)

if __name__ == '__main__':
    main()