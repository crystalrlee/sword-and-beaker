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
        self.game_text = Label(main_container, fg = "green2", bg = "grey1", wraplength = "500", height = "28", width = "92",
            font = ("Liberation Mono", 10), text = (
            "Sword & Beaker\nA Python Adventure Game\n\n"
            "You are a scientist whose funding has been cut."
            "You must travel from the City to the Mountains to Antarctica, battling enemies along the way "
            "in order to find your missing lab equipment.\n"
            "Click on the Map to get started.\n\nGood luck!"))
        self.game_text.grid(column = 1, row = 0, columnspan = 5)

        # State variables: coffee count, health, max health, location
        self.coffee = 0
        self.health = 5
        self.max_health = 5
        self.strength = 4
        self.location = "Intro"

        # Buttons
        self.map_button = Button(main_container, text="MAP", command = self.open_map)
        self.map_button.grid(column = 1, row = 2)
        self.coffee_button = Button(main_container, text="DRINK COFFEE", state = DISABLED, command = self.drink_coffee)
        self.coffee_button.grid(column = 2, row = 2)
        self.seek_fight_button = Button(main_container, text="PICK A FIGHT", state = DISABLED, command = self.fight_setup)
        self.seek_fight_button.grid(column = 3, row = 2)
        self.attack_button = Button(main_container, text = "ATTACK!", state = DISABLED)
        self.attack_button.grid(column = 4, row = 2)
        self.run_away_button = Button(main_container, text="RUN AWAY!", state = DISABLED)
        self.run_away_button.grid(column = 5, row = 2)

        # Health/Strength/Equipment Stats//Coffee count//Your location
        self.health_stats = Label(main_container, text = "Health: {}/{}".format(self.health, self.max_health),  bg = "white", font = ("Helvetica", 14))
        self.health_stats.grid(column = 0, row = 1)
        self.strength_stats = Label(main_container, text = "Strength: {}".format(self.strength), font = ("Helvetica", 14), bg = "white")
        self.strength_stats.grid(column = 0, row = 2)
        self.equipment_stats = Label(main_container, text = "Lab Equipment: 0/3", font = ("Helvetica", 14), bg = "white")
        self.equipment_stats.grid(column = 0, row = 3)
        self.coffee_count = Label(main_container, text = "Coffee: {}".format(self.coffee), bg = "white")
        self.coffee_count.grid(column = 2, row = 3)
        self.location_stats = Label(main_container, text = "Location: {}".format(self.location), bg = "white")
        self.location_stats.grid(column = 1, row = 3)

    # Called during a fight to update health stats
    def fight_health_stats(self):
        self.health_stats.config(text = "Health: {}/{}".format(self.health, self.max_health))

    def disable_buttons(self):
        self.map_button.config(state = DISABLED)
        self.coffee_button.config(state = DISABLED)
        self.seek_fight_button.config(state = DISABLED)
        # self.run_away_button.config(state = DISABLED)

    def enable_buttons(self):
        self.map_button.config(state = NORMAL)
        self.coffee_button.config(state = NORMAL)
        self.seek_fight_button.config(state = NORMAL)

    # Sets up map window, displays map image, disables game buttons
    def open_map(self):
        self.map_window = Toplevel(width = 600, height = 400)
        self.map_window.resizable(False, False)
        self.map_window.title("Map")
        self.map_image = PhotoImage(file = "map-all.gif")
        self.background_label = Label(self.map_window, image = self.map_image)
        self.background_label.bind("<Button-1>", self.enter_the_city)
        self.background_label.bind("<Destroy>", self.enter_the_city)
        self.background_label.pack()
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

    # Checks location, populates enemies for that location
    def reset_bad_guys(self):
        if self.location == "city":
            self.enemy0 = {
                "name": "an Evil Landlord", "attack phrase": "They pummel you with eviction notices.",
                "strength": 2, "health": 5}
            self.enemy1 = {
                "name":"a Pizza Rat", "attack phrase": "They attack you with something clever insert here.",
                "strength": 3, "health": 5}
        else:
            pass

    # Gets enemies, diables buttons on root window, enables Run Away and Attack! buttons
    def fight_setup(self):
        self.reset_bad_guys()
        self.disable_buttons()
        self.run_away_button.config(state = NORMAL)
        self.run_away_button.bind("<Button-1>", self.enter_the_city) # If clicked, should return player to main location text
        self.attack_button.config(state = NORMAL)
        self.fight()

    def fight(self):
        # Chooses a random enemy
        pick = random.randint(0,1)
        if pick == 0:
            enemy = self.enemy0
        else:
            enemy = self.enemy1
        # Encounter a bad get_bad_guy
        fight_text = "You encounter {}.\n They have {} strength and {} health.\n\n".format(enemy["name"], enemy["strength"], enemy["health"])
        self.game_text.config(text = fight_text)
        # Decides whether you attack first or the enemy gets the jump on you
        attack_first = random.randint(0,1)
        if attack_first == 0:
            who_attacks_first = "You attack them with your lightning fast reflexes. They lose {} health.".format(self.strength)
            enemy["health"] -= self.strength
        else:
            who_attacks_first = "{} You lose {} health.".format(enemy["attack phrase"], enemy["strength"])
            # Checks to see how much health you have (you can't go less than 1)
            if self.health > enemy["strength"]:
                self.health -= enemy["strength"]
            else:
                self.health = 0
            self.fight_health_stats()
        fight_text = fight_text + "{}".format(who_attacks_first)
        self.game_text.config(text = fight_text)

    # Called when drink coffee button is clicked
    def drink_coffee(self):
        if self.coffee == 0:
            self.game_text.config(text = "Sadly, you are out of coffee. :(\nTry picking a fight to find some.")
        elif self.health == self.max_health:
            self.game_text.config(text = "Strangely enough, you don't actually want coffee right now.")
        else:
            self.coffee -= 1
            self.health = self.max_health
            self.health_stats.config(text = "Health: {}/{}".format(self.health, self.max_health))
            self.game_text.config(text = "You're suddenly feeling much better.")

def main():
    root = Tk() # Creating a window object called root
    game = Game(root)
    root.mainloop() # Starts Tk program gameloop -- now

main()
