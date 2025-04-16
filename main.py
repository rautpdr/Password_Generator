# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
from UI_Setup import UI
from saveData import data
from password import pass_wrd


#creating UI_setup object
ui = UI()
ui.placement()

#creating save files object
file = data(ui)

#creating password object
passw = pass_wrd(ui)





ui.mainloop()