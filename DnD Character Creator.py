from tkinter import *
from CharacterCreationInfo import * 

root = Tk()
root.title("DnD Character Creator")
root.geometry("800x600")

#race selection
Label(root, text='Select Your Race', wraplength=180, justify="left", anchor="nw").grid(row=0, column=0, padx=10, pady=10, sticky="nw")

raceListbox = Listbox(root, selectmode=SINGLE, exportselection=False)
raceListbox.grid(row=1, column=0, padx=10, pady=10)
for race in listOfRaces:
        raceListbox.insert(END, race)

Button(root,text='Select Race').grid(row=2, column=0, padx=10, pady=10, sticky="nw")

root.mainloop()