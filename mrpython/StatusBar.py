from tkinter import *
from platform import python_version

class StatusBar(Frame):
    """
    Manages the status bar that gives some information about the current
    environment and editor
    """

    def __init__(self, parent, notebook):
        Frame.__init__(self, parent, background="#e1e1e1")
        self.UPDATE_PERIOD_POSITION = 100
        self.UPDATE_PERIOD_SAVE_CLEAR = 4000
        self.config(borderwidth=1, relief=GROOVE)
        self.python_label = Label(self, text="Python " + python_version(),
                                  borderwidth=1, relief=SUNKEN, width=13,
                                  background="#e1e1e1", foreground="#101010")
        self.position_label = Label(self, text="position", borderwidth=1,
                                    relief=SUNKEN, justify=CENTER, width=13,
                                    background="#e1e1e1", foreground="#101010")
        self.mode_label = Label(self, text="", borderwidth=1, relief=SUNKEN,
                                justify=CENTER, background="#e1e1e1", width=13,
                                foreground="#101010")
        self.save_label = Label(self, text="", borderwidth=1, relief=SUNKEN,
                                justify=LEFT, anchor=W, background="#e1e1e1",
                                foreground="#101010")
        self.python_label.pack(side=RIGHT, ipadx=8, ipady=3)
        self.position_label.pack(side=RIGHT, ipadx=8, ipady=3)
        self.mode_label.pack(side=RIGHT, ipadx=8, ipady=3)
        self.save_label.pack(side=RIGHT, expand=1, fill=X, ipadx=15, ipady=3)
        self.notebook = notebook
        self.update_position()
        self.displaying_save = False
        self.callback_id = 0


    def update_save_label(self, filename):
        """ Display the saved file in the save_label """
        if self.displaying_save:
            self.after_cancel(self.callback_id)
        display_text = "   Saving file '" + filename + "'"
        self.save_label.config(text=display_text)
        self.displaying_save = True
        # Then clear the text after a few seconds
        self.callback_id = self.after(self.UPDATE_PERIOD_SAVE_CLEAR,
                                      self.clear_save_label)


    def clear_save_label(self):
        """ Clear the save label text, used once the user has saved the file """
        self.save_label.config(text="")
        self.displaying_save = False


    def update_position(self):
        """ Update the position displayed in the status bar, corresponding
            to the cursor position inside the current editor """
        position = ''
        if self.notebook.index("end") > 0:
            index = self.notebook.get_current_editor().index(INSERT)
            line, col = index.split('.')
            position = "Li " + line + ", Col " + col
        self.position_label.config(text=position)
        self.after(self.UPDATE_PERIOD_POSITION, self.update_position)


    def change_mode(self, mode):
        """ Change the current mode displayed in the mode_label """
        display_text = ""
        if mode == "full":
            display_text = "Full Python"
        else:
            display_text = "Student Python"
        self.mode_label.config(text=display_text)
        
