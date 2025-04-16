from tkinter import *
from saveData import data
from password import pass_wrd

class UI(Tk):
    def __init__(self):
        super().__init__()
        self.title("PassWord Manager")
        self.config(padx= 20 , pady= 20)
        self.save_data_instance = data(self)
        self.password_instance = pass_wrd(self)


        #creating canvas object
        self.canvas = Canvas(width= 200 , height= 200)
        self.lock_img = PhotoImage(file = "logo.png")
        self.canvas.create_image(100 , 100 , image = self.lock_img)
        self.canvas.grid(row = 0 , column = 1)

    def placement(self):
        #website label
        website_label = Label(text="Website:")
        website_label.grid(row = 1 , column = 0)

        #websitr entry
        self.website_entry = Entry(width= 35)
        self.website_entry.grid(row= 1 , column = 1 ,columnspan =2)
        self.website_entry.focus()

        #email label
        email_uname_label = Label(text = "Email/Username:")
        email_uname_label.grid(row = 2 , column = 0)

        #email entry
        self.email_uname_entry = Entry(width= 35)
        self.email_uname_entry.grid(row = 2 , column = 1 , columnspan = 2)
        self.email_uname_entry.insert(0 , "xyz@gmail.com")

        #password label
        password_label = Label(text="Password:")
        password_label.grid(row= 3 , column = 0)

        #password Entry
        self.password_entry = Entry(width= 35)
        self.password_entry.grid(row = 3 , column = 1 , columnspan = 2 )

        #generate password button
        gen_password = Button(text="Generate Password" , width= 14 , command= self.password_instance.pass_gen)
        gen_password.grid(row = 3 , column = 2 )

        #generate add button
        add_button = Button(text="Add" , width= 30 , command= self.save_data_instance.save_data)
        add_button.grid(row = 4 , column = 1 , columnspan = 2)

