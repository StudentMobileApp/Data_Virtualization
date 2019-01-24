# Phillipe Shin
# 01/21/2019
# SMART Data Visualization
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import csv                                                                                                                      # This section sets up the program and reads the file into values[][]
import sys
import math
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.patches import ConnectionPatch
import numpy as np
import itertools

class project(object):
    def API(self, values):
        self.ReadFile(values)
        self.sortGraph(values)
        
    def ReadFile(self, values):                                                      
        with open('input.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            count = 0
            for line in csv_reader:
                values.append([])
                line=list(line)
                for i in line:
                    values[count].append(i)
                count = count + 1
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------               
                                                                                                # TASK 5 Part A
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def drawSPC(self, currentClass, fig, ogX, ogY):                                                       # Draws the CPC by resizing the figure and creating the graph
        for currentIndex in range(len(ogX)):
            n = len(fig.axes)
            for b in range(n):
                fig.axes[b].change_geometry(currentClass, n+1, b+1)                                  # Resizing (row, column, position)
            if (currentIndex > 0) :
                ax = fig.add_subplot(currentClass, n+1, currentIndex+1,
                    sharex = fig.axes[0], sharey= fig.axes[0])  
            else:
                ax = fig.add_subplot(currentClass, n+1, currentIndex+1)  
                
            ax.set_xlabel("X " + str(currentIndex * 2 + 1))                                                     # Styling the graph
            ax.set_ylabel("X " + str(currentIndex * 2 + 2))
            plt.xlim(min(ogX) - 1, max(ogX) + 1)
            plt.ylim(min(ogY) - 1, max(ogY) + 1)
            ax.plot(ogX[currentIndex], ogY[currentIndex],'r')                                                 # Plotting the graph
            pax = fig.axes[n]

            if (n > 0):
                xy = (ogX[n - 1], ogY[n - 1])                                                                             # These are for original values to be graphed in SPC
                ab = (ogX[n], ogY[n])
                con = ConnectionPatch(xyA=ab, xyB=xy, coordsA="data", coordsB="data",
                      axesA=fig.axes[n], axesB=fig.axes[n - 1], color="purple")
                pax.add_artist(con)                                                                                                      
                pax.plot(ogX[n],ogY[n],'ro',markersize=10)                                                       # Plot the SPC points on each graph
            else:
                pax.plot(ogX[n],ogY[n],'ro',markersize=10)                                                       # Plot the SPC points on each graph

    def sortGraph(self, values):                                                                                          # Read and process csv values
        ogX, ogY =[], []
        currentClass = 1
        xLength = len(values)                                                                                               # Number of rows
        
        for i in range(1, (xLength - 1)):                                                                                 # Exclude IDS from data
            yLength = len(values[i])                                                                                        # Number of columns
            for j in range(1, (yLength - 1)):                                                                             # Exclude IDs from data 
                if (int(values[i][yLength - 1]) == currentClass):                                                  # Process each class
                    if ((len(ogX)) <= (len(ogY))):                                                                         # X-values for graph
                        ogX.append(float(values[i][j]))                                                                  # Store the original x-value for graph
                    else:                                                                                                              # Y-values for graph
                        ogY.append(float(values[i][j]))                                                                  # Store the original y-value for graph
                else:
                    fig = plt.figure(currentClass, figsize=(12,4))                                                 # Sizing the subplots and spacing
                    fig.subplots_adjust(wspace = 0.75) 
                    fig.suptitle("SPC for Class: " + str(currentClass))
                    self.drawSPC(currentClass, fig, ogX, ogY)                                                  # Draw the CPC
                    ogX.clear()                                                                                                   # Reset everything for next class
                    ogY.clear()
                    totalX, totalY = 0, 0
                    currentClass = currentClass +1
                    ogX.append(float(values[i][j]))                                                                     # Store the first x-value of next class
                    
        fig = plt.figure(currentClass, figsize=(12,4))                                                            # Sizing the subplots and spacing
        fig.subplots_adjust(wspace = 0.75) 
        fig.suptitle("SPC for Class: " + str(currentClass))
        self.drawSPC(currentClass, fig, ogX, ogY)                                                             # Draw the last SPC (not included in for loop)  
        
        plt.show()                                                                                                                # Displays the figure
        
                                                                               
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                   
def main():
        values = [[]]
        obj = project()
        obj.API(values)

if __name__ == '__main__':
    main()