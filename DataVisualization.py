import tkinter as tk
import csv
import matplotlib

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.patches import ConnectionPatch
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)


class TopFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, bg='white', height=45, pady=3)
        self.master = master

        # Create and set all widgets for this frame
        self.createButtons()
        self.createOptionMenu()
        self.createRadioButtons()

    def createButtons(self):
        # create button widgets
        self.browseButton = tk.Button(self, text='Browse')
        self.updateButton = tk.Button(self, text='Update')
        # layout the widgets
        self.browseButton.grid(row=0, column=0)
        self.updateButton.grid(row=1, column=0)

    def createOptionMenu(self):
        # create label & option menu widgets
        self.meaningLabel = tk.Label(self, text='Meaning of Weights:')
        self.weightMeaning = tk.StringVar(self)
        self.weightMeaning.set("distance between nodes")  # default value of drop down
        self.dropDown1 = tk.OptionMenu(self, self.weightMeaning, "distance between nodes", "frequency of communication",
                                       "frequency of visits")
        # layout widgets
        self.meaningLabel.grid(row=0, column=2, padx=(50, 0))
        self.dropDown1.grid(row=0, column=3)

    def createRadioButtons(self):
        # create label & radio buttons widgets
        self.similarityLabel = tk.Label(self, text='Higher Value of the Weight indicates:')
        self.var1 = tk.IntVar()
        self.similarityButton1 = tk.Radiobutton(self, text="higher similarity", variable=self.var1, value=1)
        self.similarityButton2 = tk.Radiobutton(self, text="higher dissimilarity", variable=self.var1, value=2)
        # layout widgets
        self.similarityLabel.grid(row=0, column=4, padx=(50, 0))
        self.similarityButton1.grid(row=1, column=4, sticky='w', padx=(60, 0))
        self.similarityButton2.grid(row=2, column=4, sticky='w', padx=(60, 0))


class CenterFrame(tk.Frame):

    def __init__(self, master, bottomFrame):
        tk.Frame.__init__(self, bg='gray1', padx=3, pady=3)
        self.master = master
        self.createCenterFrameSections()
        self.bottomFrame = bottomFrame

        # create cpc from Phillipe
        #self.values = [[]]
        #self.cpcAPI()
        #self.spcAPI()

    def createCenterFrameSections(self):
        # create the center widgets
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.ctr_left = tk.Frame(self, bg='gray', width=100)
        self.ctr_mid = tk.Frame(self, bg='white')
        self.ctr_right = tk.Frame(self, bg='gray', width=100)

        self.ctr_left.grid(row=0, column=0, sticky="ns")
        self.ctr_mid.grid(row=0, column=1, sticky="nsew")
        self.ctr_right.grid(row=0, column=2, sticky="ns")

    def cpcAPI(self):
        for widget in self.ctr_mid.winfo_children():                # Clears widgets on the frame
            widget.destroy()
        for widget in self.bottomFrame.winfo_children():                # Clears widgets on the bottom frame
            widget.destroy()
        self.values = [[]]
        self.ReadFile1()
        self.Output()
        self.createCPC()

    def cpcAPI2(self):
        for widget in self.ctr_mid.winfo_children():                # Clears widgets on the frame
            widget.destroy()
        for widget in self.bottomFrame.winfo_children():                # Clears widgets on the bottom frame
            widget.destroy()
        self.values = [[]]
        self.ReadFile1()
        self.Output()
        self.createSeperateCPC()

    def spcAPI(self):
        for widget in self.ctr_mid.winfo_children():                # Clears widgets on the frame
            widget.destroy()
        for widget in self.bottomFrame.winfo_children():                # Clears widgets on the bottom frame
            widget.destroy()
        self.values = [[]]
        self.ReadFile2()
        self.Output()
        self.createSPC()

    def ReadFile1(self):  # Reads values into 2d array
        with open('input.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            count = 0
            for line in csv_reader:
                self.values.append([])
                line = list(line)
                for i in line:
                    self.values[count].append(i)
                count = count + 1

    def ReadFile2(self):  # Reads values into 2d array
        with open('input2.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            count = 0
            for line in csv_reader:
                self.values.append([])
                line = list(line)
                for i in line:
                    self.values[count].append(i)
                count = count + 1

    def Output(self):
        print("The file contains...")
        for i in range(len(self.values)):
            print("");
            for j in range(len(self.values[i])):
                currentLine = str(self.values[i][j])
                print(currentLine, end=" ")
        print(" ")

    def setToolbar(self, graph):
        toolbar1 = NavigationToolbar2Tk(graph, self.bottomFrame)
        toolbar1.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def createSPC(self):
        print("")
        print("The matrix has been converted into x and y coordinates")
        ogX = []
        ogY = []
        first = []
        second = []
        xNums = 0
        yNums = 0
        totalx = 0
        totaly = 0

        for i in range(len(self.values)):
            for j in range(len(self.values[i])):
                if (int(self.values[i][j]) > 0):
                    if (xNums <= yNums):  # X-values for graph
                        totalx = int(self.values[i][j]) + int(totalx)  # Total  distance x
                        first.append(int(totalx))
                        ogX.append(int(self.values[i][j]))  # Original x-values (for SPC)
                        xNums = xNums + 1
                    else:  # Y-values for graph
                        totaly = int(self.values[i][j]) + int(totaly)  # Total  distance y
                        second.append(int(totaly))
                        ogY.append(int(self.values[i][j]))  # Original y-values (for SPC)
                        yNums = yNums + 1

                else:
                    continue

        print("CPC Values")  # Printing coordinate pairs
        for m in range(len(first)):
            print("(" + str(first[m]) + "," + str(second[m]) + ")")

        print("\n SPC values")
        for m in range(len(ogX)):
            print("(" + str(ogX[m]) + "," + str(ogY[m]) + ")")

        fig = plt.figure()  # Creating the sub plot and plot points
        p1 = fig.add_subplot(131)
        p2 = fig.add_subplot(132)
        p3 = fig.add_subplot(133)

        p1.plot(ogX[0], ogY[0])
        p2.plot(ogX[1], ogY[1])

        xy = (ogX[0], ogY[0])  # These are for original values to be graphed in SPC
        ab = (ogX[1], ogY[1])
        cd = (ogX[2], ogY[2])
        con = ConnectionPatch(xyA=ab, xyB=xy, coordsA="data", coordsB="data",
                              axesA=p2, axesB=p1, color="purple")
        p2.add_artist(con)

        p1.plot(ogX[0], ogY[0], 'ro', markersize=10)  # Plot the SPC points on each graph
        p2.plot(ogX[1], ogY[1], 'ro', markersize=10)
        p3.plot(ogX[2], ogY[2], 'ro', markersize=10)

        print("\nPrinting the SPC for the first two coordinate pairs")
        #plt.show()
        spc = FigureCanvasTkAgg(fig, self.ctr_mid)  # A tk.DrawingArea.
        spc.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.setToolbar(spc)

    def createCPC(self):
        xCoords = []
        yCoords = []
        totalX = 0
        totalY = 0
        currentClass = 1
        xLength = len(self.values)  # Rows

        fig = plt.Figure()
        a = fig.add_subplot(111)  # .plot(x, y) # 1 by 1, graph #1?
        a.set_title("Collocated Paired Coordinates")
        a.set_xlabel('x')
        a.set_ylabel('y')

        for i in range(1, (xLength - 1)):  # 1- 6
            yLength = len(self.values[i])  # Columns
            for j in range(1, (yLength - 1)):
                if (int(self.values[i][yLength - 1]) == currentClass):
                    if ((len(xCoords)) <= (len(yCoords))):  # X-values for graph
                        totalX = float(self.values[i][j]) + float(totalX)  # Total  distance x
                        xCoords.append(float(totalX))
                    else:  # Y-values for graph
                        totalY = float(self.values[i][j]) + float(totalY)  # Total  distance y
                        yCoords.append(float(totalY))
                else:
                    a.plot(xCoords, yCoords)
                    print("Class: ", currentClass, " CPC values...")  # Printing for our use
                    for m in range(len(xCoords)):
                        print("(" + str(xCoords[m]) + "," + str(yCoords[m]) + ")")
                    xCoords.clear()  # Reset everything for next class
                    yCoords.clear()
                    totalX = 0
                    totalY = 0
                    currentClass = currentClass + 1
                    xCoords.append(float(self.values[i][j]))  # Append the first X-coord of class

        a.plot(xCoords, yCoords)
        cpc = FigureCanvasTkAgg(fig, self.ctr_mid)  # A tk.DrawingArea.
        cpc.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.setToolbar(cpc)

    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # TASK 5 Part A : Draw All Graphs in CPC separately
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def drawCPC(self, currentClass, fig, xCoords, yCoords):  # Draws the CPC by resizing the figure and creating the graph
        n = len(fig.axes)
        for b in range(n):
            fig.axes[b].change_geometry(n + 1, 1, b + 1)  # Resizing (row, column, position)
        ax = fig.add_subplot(n + 1, 1, n + 1)
        ax.set_xlabel('x')  # Styling the graph
        ax.set_ylabel('y')
        ax.set_title("CPC for Class: " + str(currentClass))
        ax.plot(xCoords, yCoords, '--bo')  # Plotting the graph

    def createSeperateCPC(self):  # This is the "core" method of this task. Calculates CPC values and draws the graph
        xCoords, yCoords = [], []  # Stores the X and Y coordinates
        totalX, totalY, currentClass = 0, 0, 1
        xLength = len(self.values)  # Number of rows

        fig = plt.figure(figsize=(7, 7))  # Sizing the subplots and spacing
        fig.subplots_adjust(hspace=0.5)

        for i in range(1, (xLength - 1)):  # Exclude IDS from data
            yLength = len(self.values[i])  # Number of columns
            for j in range(1, (yLength - 1)):  # Exclude IDs from data
                if (int(self.values[i][yLength - 1]) == currentClass):  # Process each class
                    if ((len(xCoords)) <= (len(yCoords))):  # X-values for graph
                        totalX = float(self.values[i][j]) + float(totalX)
                        xCoords.append(float(totalX))  # Store the current total X distance
                    else:  # Y-values for graph
                        totalY = float(self.values[i][j]) + float(totalY)
                        yCoords.append(float(totalY))  # Store the current total Y distance
                else:
                    self.drawCPC(currentClass, fig, xCoords, yCoords)  # Draw the CPC
                    xCoords.clear()  # Reset everything for next class
                    yCoords.clear()
                    totalX, totalY = 0, 0
                    currentClass = currentClass + 1
                    xCoords.append(float(self.values[i][j]))  # Store the first x-value of next class

        self.drawCPC(currentClass, fig, xCoords, yCoords)  # Draws the last CPC
        #plt.show()  # Displays the figure
        dividedCPC = FigureCanvasTkAgg(fig, self.ctr_mid)  # A tk.DrawingArea.
        dividedCPC.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.setToolbar(dividedCPC)



class BottomFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, bg='white', height=45, pady=3)
        self.master = master


class MainApplication(tk.Frame):

    def __init__(self, master, *args, **kwargs):
        root.title('Data Visualization')
        root.geometry('{}x{}'.format(1000, 1000))
        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)

        tk.Frame.__init__(self, master, *args, **kwargs)  # define settings upon initialization
        self.master = master  # reference to the master widget, the tk window

        # Call classes to create frames
        self.topFrame = TopFrame(self)
        self.bottomFrame = BottomFrame(self)
        self.centerFrame = CenterFrame(self, self.bottomFrame)


        tk.Menu.__init__(self, master)
        self.createMenu()

        # root.grid_rowconfigure(1, weight=1)
        # root.grid_columnconfigure(0, weight=1)

        # Set frames in position
        self.topFrame.grid(row=0, sticky="ew")
        self.centerFrame.grid(row=1, sticky="nsew")
        self.bottomFrame.grid(row=2, sticky="ew")
        root.config(menu=self.menubar)

    def createMenu(self):
        self.menubar = tk.Menu(self)

        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="New")
        self.filemenu.add_command(label="Open")
        self.filemenu.add_command(label="Save")
        self.filemenu.add_command(label="Save as...")
        self.filemenu.add_command(label="Close")
        self.filemenu.add_separator() # adds a line ---
        self.filemenu.add_command(label="Exit", command=self.quit)
        self.menubar.add_cascade(label="File", menu=self.filemenu) # add the FILE menu

        self.viewmenu = tk.Menu(self.menubar, tearoff=0)
        self.viewmenu.add_command(label="Collocated Paired Coordinates (CPC)", command=self.centerFrame.cpcAPI)
        self.viewmenu.add_command(label="Seperated CPC(s)", command=self.centerFrame.cpcAPI2)
        self.viewmenu.add_separator()  # adds a line ---
        self.viewmenu.add_command(label="Shifted Paired Coordinates (SPC)", command=self.centerFrame.spcAPI)
        self.menubar.add_cascade(label="View", menu=self.viewmenu) # add the VIEW menu

        self.editmenu = tk.Menu(self.menubar, tearoff=0)
        self.editmenu.add_command(label="Undo")
        self.editmenu.add_separator() # adds a line ---
        self.editmenu.add_command(label="Cut")
        self.editmenu.add_command(label="Copy")
        self.editmenu.add_command(label="Paste")
        self.editmenu.add_command(label="Delete")
        self.editmenu.add_command(label="Select All")
        self.menubar.add_cascade(label="Edit", menu=self.editmenu) # add the EDIT menu

        self.helpmenu = tk.Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="Help Index")
        self.helpmenu.add_command(label="About...")
        self.menubar.add_cascade(label="Help", menu=self.helpmenu) # add the HELP menu



if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root)
    while True:  # Scrolling on trackpad (Mac) throws error
        try:
            root.mainloop()
            break
        except UnicodeDecodeError:
            pass