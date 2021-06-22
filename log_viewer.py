# Name:  Morium Mostfafa Momo
# Student Number:  10492778

# This file is provided to you as a starting point for the "log_viewer.py" program of Assignment 2
# of Programming Principles in Semester 1, 2019.  It aims to give you just enough code to help ensure
# that your program is well structured.  Please use this file as the basis for your assignment work.
# You are not required to reference it.

# The "pass" command tells Python to do nothing.  It is simply a placeholder to ensure that the starter files run smoothly.
# They are not needed in your completed program.  Replace them with your own code as you complete the assignment.


# Import the required modules.
import tkinter # Used to create the GUI.
from tkinter import *
from tkinter import Tk, Label, Button, messagebox, Frame
import tkinter.messagebox # Used to show pop-up information windows.
import json # Used to convert between JSON-formatted text and Python variables. 

class ProgramGUI:
    def __init__(self,master):
        # This is the constructor of the class.
        # It is responsible for loading the log file data and creating the user interface.
        # See the "Constructor of the GUI Class of log_viewer.py" section of the assignment brief.
        self.master = master
        master.title("Word Find Log Viewer")
        frame = Frame(master)
        frame.pack()

        self.label_letters = Label(frame, width=50, text="", anchor="w")
        self.label_letters.pack()
        self.label_words = Label(frame, width=50, text="", anchor="w")
        self.label_words.pack()
        self.label_score = Label(frame, width=50, text="", anchor="w")
        self.label_score.pack()

        bottomframe = Frame(root)
        bottomframe.pack( side = BOTTOM )

        self.pre_button = Button(bottomframe, width = 10, padx = 2, text="Previous", command=self.previous_log)
        self.pre_button.pack( side = LEFT)
        self.label_id = Label(bottomframe, text="")
        self.label_id.pack(side = LEFT)
        self.nxt_button = Button(bottomframe, width = 10, padx = 2, text="Next", command=self.next_log)
        self.nxt_button.pack( side = LEFT )

        try:
            with open("logs.txt", "r") as read_file:
                self.logs = json.load(read_file)
                self.current_log = 0
                read_file.close()
        except:
            messagebox.showerror("Error", "Missing/Invalid file")
            master.destroy()
            return

        self.show_log()

    # This method displays the current log
    def show_log(self):
        # This method displays the details of the current log in the GUI.
        # See Point 1 of the "Methods in the GUI class of fruit_test.py" section of the assignment brief.
        #print(self.logs[self.current_log]['letters'])
        self.label_letters['text'] =  'Letters: ' + ', '.join(self.logs[self.current_log]['letters']) 
        self.label_words['text'] =  'Words: ' + ', '.join(self.logs[self.current_log]['words']) 
        self.label_score['text'] =  'Score: ' + str(self.logs[self.current_log]['score'])
        self.label_id['text'] = 'Log ' + str(self.current_log+1) + '/' + str(len(self.logs))


    def previous_log(self):
        # This method is called when the user clicks the "Previous" button.
        # See Point 2 of the "Methods in the GUI class of fruit_test.py" section of the assignment brief.
        if self.current_log == 0:
            messagebox.showerror('End of File','No previous log.')
        else:
            self.current_log -= 1
            self.show_log()



    def next_log(self):
        # This method is called when the user clicks the "Next" button.
        # See Point 3 of the "Methods in the GUI class of fruit_test.py" section of the assignment brief.
        if self.current_log == len(self.logs)-1:
            messagebox.showerror('End of File','No next log.')
        else:
            self.current_log += 1
            self.show_log()



root = Tk()
gui = ProgramGUI(root)
root.mainloop()
