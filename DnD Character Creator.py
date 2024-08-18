from tkinter import *
from CharacterCreationInfo import * 

root = Tk()
root.title("DnD Character Creator")
root.geometry("800x600")

leftFrame = Frame(root)
leftFrame.grid(row=0, column=0, padx=10, pady=10, sticky="ns")

rightFrame = Frame(root)
rightFrame.grid(row=0, column=1, padx=10, pady=10, sticky="ns")

#initalize character info
character = {'Name': 'N/A',
             'Race': 'N/A',
             'Sex': 'N/A',
             'Level': '1', 
             'Class': 'N/A',
             }
character_info_var = StringVar()
character_info_var.set("\n".join([f"{key}: {value}" for key, value in character.items()]))
characterInfoLabel = Label(rightFrame, textvariable=character_info_var, anchor="nw", justify="left")
characterInfoLabel.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

#race selection
Label(leftFrame, text='Select Your Race', wraplength=180, justify="left", anchor="nw").grid(row=0, column=0, padx=10, pady=10, sticky="nw")
raceListbox = Listbox(leftFrame, selectmode=SINGLE, exportselection=False)
raceListbox.grid(row=1, column=0, padx=10, pady=10)
for race in listOfRaces:
        raceListbox.insert(END, race)
Button(leftFrame,text='Select Race').grid(row=2, column=0, padx=10, pady=10, sticky="nw")

root.mainloop()