from tkinter import *

class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.instruction = Label(self, text="Enter the text file name")
        self.instruction.grid(row = 0, column = 0, columnspan = 1, sticky = W)

        self.fileName = Entry(self)
        self.fileName.grid(row = 0, column = 1, sticky = W)
        
        self.check_button = Button(self, text="Check", command = self.reveal)
        self.check_button.grid(row = 0, column = 3, sticky = W)
        
        self.text = Text(self, width = 30, height = 2, wrap = WORD)
        self.text.grid(row = 1, column = 0, columnspan = 3, sticky = W)

        Label(self, text="Choose the meaning of the weights").grid(row = 4, column = 0, sticky = W)
        Label(self, text="Select one of the following:").grid(row  = 5, column = 0, sticky = W)

        self.choice = StringVar()
        
        Radiobutton(self, text="Distance between nodes",
                    value = 1,
                    variable = self.choice,
                    command = self.update_text).grid(row = 6, column = 0, sticky = W)
        Radiobutton(self, text="Frequency of communication",
                    value = 2,
                    variable = self.choice,
                    command = self.update_text).grid(row = 7, column = 0, sticky = W)

        Radiobutton(self, text="Frequency of  visits",
                    value = 3,
                    variable = self.choice,
                    command = self.update_text).grid(row = 8, column = 0, sticky = W)

        self.result = Text(self, width =40, height = 5, wrap = WORD)
        self.result.grid(row = 9, column = 0, columnspan = 3)


        Label(self, text="Higher weights indicate...").grid(row = 10, column = 0, sticky = W)

        self.choice2 = StringVar()
        
        Radiobutton(self, text="Higher Similarity",
                    value = 4,
                    variable = self.choice2,
                    command = self.update_text).grid(row = 11, column = 0, sticky = W)
        Radiobutton(self, text="Higher Dissimilarity",
                    value = 5,
                    variable = self.choice2,
                    command = self.update_text).grid(row = 12, column = 0, sticky = W)


        self.result = Text(self, width =40, height = 5, wrap = WORD)
        self.result.grid(row = 9, column = 0, columnspan = 3)

    def update_text(self):
        message = "Your choice is "
        message += self.choice.get()
        self.result.delete(0.0, END)
        self.result.insert(0.0, message)
        
    def reveal(self):
        content = self.fileName.get()

        if ".txt" in content:
            message = "File name accepted"

        else:
            message = "File name invalid"
        self.text.delete(0.0, END)
        self.text.insert(0.0, message)

root = Tk()
root.title("Data Visualization")
root.geometry("500x550")
app = Application(root)

root.mainloop()

