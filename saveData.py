import tkinter.messagebox
from tkinter import *


class data():
    def __init__(self , ui_gui):
        self.gui = ui_gui

    def save_data(self):
        self.website = self.gui.website_entry.get()
        self.email_uname = self.gui.email_uname_entry.get()
        self.password = self.gui.password_entry.get()

        if len(self.website) == 0 or len(self.email_uname) == 0 or len(self.password) == 0:
            tkinter.messagebox.showwarning(title = "Invalid Operation." , message= "Please fill all the fields!")

        else :
            confirm = tkinter.messagebox.askokcancel("Confirmation" , "Make sure of added details\n"
                                                                      f"website = {self.website}\nemail = {self.email_uname}\npassword = {self.password}")
            if confirm:
                with open("data.txt" , "a") as data_file:
                    data_file.write(f"{self.website} | {self.email_uname} | {self.password} \n")
                self.clear_data()






    def clear_data(self):
        self.gui.website_entry.delete(0, END)
        self.gui.password_entry.delete(0, END)







