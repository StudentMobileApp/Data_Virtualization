import sys
import pandas as pd
from matplotlib import pyplot as plt

class project(object):
    def API(self, values):
        self.ReadFile(values)
        self.Output(values)
        self.sortGraph(values)
        
    def ReadFile(self, values):                         #Reads values into 2d array
        fileName = 'input.txt'
        lineCount = 0
        with open(fileName, "r") as  file:
            count = 0
            for line in file:
                values.append([])
                for i in line.split():
                    if i.isdigit():
                        values[count].append(int(i))
                count = count + 1
        file.close()
        
    def Output(self, values):
        print("The file contains...")
        for i in range(len(values)):
            print("");
            for j in range(len(values[i])):
                currentLine = str(values[i][j])
                print(currentLine, end=" ")

    def sortGraph(self, values):                        #For undirected graphs
        print("The matrix has been split into two arrays")
        first = []
        second = []
        xNums = 0
        yNums = 0
        totalx = 0
        totaly = 0
        for i in range(len(values)):
            for j in range(len(values[i])):
                if (values[i][j] > 0):
                    if (xNums <= yNums):                #X-values for graph
                        totalx = int(values[i][j]) + int(totalx)    #Total  distance x
                        first.append(int(totalx))
                        print("First[" + str(xNums) + "] is " + str(first[xNums]))
                        xNums = xNums + 1
                    else:                               #Y-values for graph
                        totaly = int(values[i][j]) + int(totaly)    #Total  distance y  
                        second.append(int(totaly))
                        print("Second[" + str(yNums) +"] is " + str(second[yNums]))
                        yNums = yNums + 1
                        
                else:
                   continue

        plt.plot(first, second)
        plt.title("Collocated Paired Coordinates")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.show()
            
def main():
    values = [[]]
    obj = project()
    obj.API(values)

if __name__ == '__main__':
    main()
