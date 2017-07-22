# game.py
# Sword & Beaker adventure game

from tkinter import *
import random

class Game():
    def __init__(self, root):
        self.root = root
        # Sets root window properties
        root.title("Sword & Beaker")
        root.geometry("1100x530")
        root.resizable(False, False) # Makes window fixed size

        # Main container frame properties
        main_container = Frame(root, bg = "white")
        main_container.grid()

        # Avatar label
        self.avatar_image = PhotoImage(file = "warrior_girl.gif")
        self.avatar = Label(main_container, image = self.avatar_image, bd = 10)
        self.avatar.grid(column = 0, row = 0)

        # Game text area
        self.game_text = Label(main_container, fg = "green2", bg = "grey1", height = "30", width = "92", text = """Sword & Beaker\nA Python Adventure Game\n
        \nYou are a scientist whose funding has been cut. You must travel from The City to The Mountains to Antarctica,
        battling enemies along the way in order to find the lab equipment to carry out your condensed matter experiment.
        \n Good luck!""")
        self.game_text.grid(column = 1, row = 0, columnspan = 5)

        # Buttons
        self.map_button = Button(main_container, text="MAP", command = self.open_map)
        self.map_button.grid(column = 1, row = 2)
        self.coffee_button = Button(main_container, text="DRINK COFFEE")
        self.coffee_button.grid(column = 2, row = 2)
        self.seek_fight_button = Button(main_container, text="PICK A FIGHT", command = self.start_fight)
        self.seek_fight_button.grid(column = 3, row = 2)
        self.attack_button = Button(main_container, text = "ATTACK!", state = DISABLED)
        self.attack_button.grid(column = 4, row = 2)
        self.run_away_button = Button(main_container, text="RUN AWAY!", state = DISABLED)
        self.run_away_button.grid(column = 5, row = 2)

        # Health/Strength/Equipment Stats
        self.health_stats = Label(main_container, text = "Health: 5/5",  bg = "white", font = ("Helvetica", 14))
        self.health_stats.grid(column = 0, row = 1)
        self.strength_stats = Label(main_container, text = "Strength: 4/4", font = ("Helvetica", 14), bg = "white")
        self.strength_stats.grid(column = 0, row = 2)
        self.equipment_stats = Label(main_container, text = "Lab Equipment: 0/3", font = ("Helvetica", 14), bg = "white")
        self.equipment_stats.grid(column = 0, row = 3)

    def disable_buttons(self):
        self.map_button.config(state = DISABLED)
        self.coffee_button.config(state = DISABLED)
        self.seek_fight_button.config(state = DISABLED)
        # self.run_away_button.config(state = DISABLED)

    def enable_buttons(self):
        self.map_button.config(state = NORMAL)
        self.coffee_button.config(state = NORMAL)
        self.seek_fight_button.config(state = NORMAL)

    def open_map(self):
        # Sets map window
        self.map_window = Toplevel(width = 600, height = 400)
        self.map_window.resizable(False, False)
        self.map_window.title("Map")
        # Sets map image
        self.map_image = PhotoImage(file = "map-all.gif")
        self.background_label = Label(self.map_window, image = self.map_image)
        self.background_label.bind("<Button-1>", self.enter_the_city)
        self.background_label.bind("<Destroy>", self.enter_the_city)
        self.background_label.pack()
        # Disables buttons on root window
        self.disable_buttons()

    def enter_the_city(self, event):
        # Closes map window
        self.map_window.destroy()
        # Enables buttons on root window
        self.enable_buttons()
        # Changes game text
        self.game_text.config(text = (
            "You enter \"The City\"!\n\nA concrete realm of sunshine, adventure, and probably gentrification.\n\n"
            "From here you can heal your wounds with a cup of coffee,\n"
            "pick a fight with the locals, \n"
            "or go somewhere else with your map. \n\n"
            "Enjoy it before your rent goes up again."))
        self.location = "city"

    def start_fight(self):
        # Disables buttons on root window
        self.disable_buttons()
        # Enables Run Away and Attack! buttons
        self.run_away_button.config(state = NORMAL)
        self.attack_button.config(state = NORMAL)



def main():
    root = Tk() # Creating a window object called root
    game = Game(root)
    root.mainloop() # Starts Tk program gameloop -- now

main()
