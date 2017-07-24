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
        self.coffee = 1
        self.health = 10
        self.max_health = 10
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
        self.run_away_button.config(state = DISABLED)

    def enable_buttons(self):
        self.map_button.config(state = NORMAL)
        self.coffee_button.config(state = NORMAL)
        self.seek_fight_button.config(state = NORMAL)
        self.run_away_button.config(state = DISABLED)
        self.attack_button.config(state = DISABLED)

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
            "You enter \"The City\"!\n\nA concrete realm of sunshine, adventure, and gentrification.\n\n"
            "From here you can heal your wounds with a cup of coffee,\n"
            "pick a fight with the locals, \n"
            "or go somewhere else on your map. \n\n"
            "Enjoy it before your rent goes up again."))
        self.location = "The City"
        self.location_stats.config(text = "Location: {}".format(self.location))

    # Checks location, populates enemies for that location
    def get_enemy(self):
        pick = random.randint(0,2)
        if self.location == "The City":
            if pick == 0:
                self.enemy = {
                    "name": "an Evil Landlord", "attack phrase": "They pummel you with eviction notices.",
                    "strength": 2, "health": 5}
            if pick == 2:
                self.enemy = {
                    "name": "a Pizza Rat", "attack phrase": "They attack you with clever memes.",
                    "strength": 3, "health": 4}
            else:
                self.enemy = {
                    "name": "bedbugs", "attack phrase": "Did you know that bedbugs can survive for months without food or water?",
                    "strength": 2, "health": 6}
                }
        else:
            pass
        return self.enemy

    # Gets enemies, diables buttons on root window, enables Run Away and Attack! buttons
    def fight_setup(self):
        self.disable_buttons()
        self.run_away_button.config(state = NORMAL)
        self.run_away_button.bind("<Button-1>", self.enter_the_city) # If clicked, should return player to main location text
        self.attack_button.config(state = NORMAL)
        self.enemy = self.get_enemy()
        # Encounter an ememy
        self.fight_text = "You encounter {}.\n They have {} strength and {} health.\n\n".format(self.enemy["name"], self.enemy["strength"], self.enemy["health"])
        self.game_text.config(text = self.fight_text)
        self.attack_button.bind("<Button-1>", self.attack)

    # Handles the logic of fights when player presses Attack button
    def attack(self, event):
        # Decides whether you attack first or the enemy gets the jump on you
        if self.health > 0 and self.enemy["health"] > 0:
            attack_first = random.randint(0,1)
            if attack_first == 0:
                who_attacks_first = "You attack them with your lightning fast reflexes. They lose {} health.".format(self.strength)
                self.enemy["health"] -= self.strength
            else:
                who_attacks_first = "{} You lose {} health.".format(self.enemy["attack phrase"], self.enemy["strength"])
                # Checks to see how much health you have (you can't go less than 0)
                if self.health > self.enemy["strength"]:
                    self.health -= self.enemy["strength"]
                # Makes sure player health can't go less than 0
                else:
                    self.health = 0
                self.fight_health_stats()
            #Updates fight text
            self.game_text.config(text = "{}".format(who_attacks_first))
        # Checks to see if player won fight or list game
        if self.enemy["health"] <= 0:
            self.game_text.config(text = "{}\n\nYou win!".format(who_attacks_first))
            self.enable_buttons()
        if self.health < 1:
            self.game_text.config(text = "{}\n\nI need to do an end game thingy. Program. Thing.\nThe End.".format(who_attacks_first))

    # Deals with the logic of loot drops
    # def get_loot(self):
    #     possible_loot = {
    #         "special item": None ,
    #         "coffee": "It's good for what ails ya.",
    #         "safety goggles": "Way to have good lab safety practices. Your max health increases.",
    #         "pocket protector": "You're not sure what this does, but you feel much safer anyway."
    #         "basic sword": "It's not a very good sword, but it is heavy. After carrying it for awhile you feel much stronger!"
    #         "mylar lab coat": ""
    #     }
    #
    #     d = {
    #         'cateogry1': [
    #             {
    #                 'name': 'banana',
    #                 'desc': 'it is yellow'
    #             },
    #             {
    #                 'name': 'bird',
    #                 'desc': 'it flies'
    #             }
    #         ],
    #         'category2': []
    #     }
    #     item = random.choice(d['category1'])
    #     item['name']
    #     item['desc']
    #
    #     if location == "city" and self.equipment_stats < 1:
    #         possible_loot["special item"] = "Electrostatic Analyzer"
    #     else:
    #         pass
    #     # Probability of coffee 1:2, probability of strength/max_health increase 1:4, probability of special item 1:6
    #     coffee_roll = random.randint(0,1):
    #     if coffee_roll == 1:
    #         pass

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
            self.game_text.config(text = "Coffee makes everything feel better.")
            self.coffee_count.config(text = "Coffee: {}".format(self.coffee))

def main():
    root = Tk() # Creating a window object called root
    game = Game(root)
    root.mainloop() # Starts Tk program gameloop -- now

main()
