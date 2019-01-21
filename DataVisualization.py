import tkinter as tk
import csv
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class TopFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, bg='white',height=45, pady=3)
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
        self.dropDown1 = tk.OptionMenu(self, self.weightMeaning, "distance between nodes", "frequency of communication","frequency of visits")
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
    def __init__(self, master):
        tk.Frame.__init__(self, bg='gray1', padx=3, pady=3)
        self.master = master
        self.createCenterFrameSections()

        # create cpc from Phillipe
        self.values = [[]]
        self.API()

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

    def API(self):
        self.ReadFile()
        self.Output()
        self.createCPC()

    def ReadFile(self):  # Reads values into 2d array
        with open('input.csv', 'r') as csv_file:
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

class BottomFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, bg='white', height=45, pady=3)
        self.master = master

class MainMenu(tk.Menu):
    def __init__(self, master):
        tk.Menu.__init__(self, master)
        #self.master = master
        self.createMenu()

    def createMenu(self):
        self.menubar = tk.Menu(self)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="New", command=self.donothing)
        self.filemenu.add_command(label="Open", command=self.openFile)
        self.filemenu.add_command(label="Save", command=self.donothing)
        self.filemenu.add_command(label="Save as...", command=self.donothing)
        self.filemenu.add_command(label="Close", command=self.donothing)

        self.filemenu.add_separator()

        self.filemenu.add_command(label="Exit", command=self.quit)
        self.add_cascade(label="File", menu=self.filemenu)
        self.editmenu = tk.Menu(self.menubar, tearoff=0)
        self.editmenu.add_command(label="Undo", command=self.donothing)

        self.editmenu.add_separator()

        self.editmenu.add_command(label="Cut", command=self.donothing)
        self.editmenu.add_command(label="Copy", command=self.donothing)
        self.editmenu.add_command(label="Paste", command=self.donothing)
        self.editmenu.add_command(label="Delete", command=self.donothing)
        self.editmenu.add_command(label="Select All", command=self.donothing)

        self.add_cascade(label="Edit", menu=self.editmenu)
        self.helpmenu = tk.Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="Help Index", command=self.donothing)
        self.helpmenu.add_command(label="About...", command=self.donothing)
        self.add_cascade(label="Help", menu=self.helpmenu)

        #self.config(menu= self.menubar)


    def openFile(self):
        from tkinter.filedialog import askopenfilename
        self.file = askopenfilename()
        print(self.file)
        # showGraphs(file)

    def donothing(self):
        self.filewin = tk.Toplevel(root)
        button = tk.Button(self.filewin, text="Do nothing button")
        button.pack()


class MainApplication(tk.Frame):

    def __init__(self, master, *args, **kwargs):
        root.title('Data Visualization')
        root.geometry('{}x{}'.format(1000, 1000))
        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)

        tk.Frame.__init__(self, master, *args, **kwargs) # define settings upon initialization
        self.master = master # reference to the master widget, the tk window

        # Call classes to create frames
        self.topFrame = TopFrame(self)
        self.centerFrame = CenterFrame(self)
        self.bottomFrame = BottomFrame(self)
        self.mainMenu = MainMenu(self)

        #root.grid_rowconfigure(1, weight=1)
        #root.grid_columnconfigure(0, weight=1)

        # Set frames in position
        self.topFrame.grid(row=0, sticky="ew")
        self.centerFrame.grid(row=1, sticky="nsew")
        self.bottomFrame.grid(row=2, sticky="ew")
        root.config(menu=self.mainMenu)


if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root)
