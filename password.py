#Password Generator Project
import random
from random import *
from tkinter import *

class pass_wrd:
    def __init__(self , ui_gui):
        self.ui_instace = ui_gui




    def pass_gen(self):

        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        pass_letter = [choice(letters) for _ in range(randint(8,10))]
        pass_number = [choice(numbers) for _ in range(randint(2,4))]
        pass_symbol = [choice(symbols) for _ in range(randint(1,8))]

        password_list = pass_letter+pass_number+pass_symbol

        self.password = "".join(password_list)

        self.ui_instace.password_entry.delete(0 , END)
        self.ui_instace.password_entry.insert(0, self.password)




