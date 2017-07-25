# game.py
# Sword & Beaker adventure game

from tkinter import *
import random

class Game():
    def __init__(self, root):
        self.root = root
        # Sets root window properties
        root.title("Sword & Beaker")
        root.geometry("1150x635")
        root.resizable(False, False) # Makes window fixed size

        # Main container frame properties
        main_container = Frame(root, bg = "white")
        main_container.grid()

        # Avatar label
        self.avatar_image = PhotoImage(file = "avatar.gif")
        self.avatar = Label(main_container, image = self.avatar_image, borderwidth = 0)
        self.avatar.grid(column = 5, row = 2, rowspan = 4)

        # Sets up map, loads images
        self.map_image = PhotoImage(file = "map-city-only.gif")
        self.map_image2 = PhotoImage(file = "map-city-mountains.gif")
        self.map_image3 = PhotoImage(file = "map-city-mountains-antarctica.gif")
        self.map_image4 = PhotoImage(file = "map-all-color1.gif")
        self.map_label = Label(main_container, image = self.map_image, borderwidth = 5, cursor = "hand1")
        self.map_label.grid(column = 4, columnspan = 2, row = 0)
        self.map_label.bind("<Button-1>", self.on_map_click)

        # Game text area
        self.game_text = Label(main_container, fg = "green2", bg = "grey1", width = 68, height = 29, wraplength = 475,
            font = ("Liberation Mono", 12), text = (
            "Sword & Beaker\nA Python Adventure Game\n\n"
            "You are a scientist whose funding has been cut."
            "In order to find your missing lab equipment you must travel from the City to the Mountains to Antarctica, battling enemies along the way.\n\n"
            "Click on the Map to get started.\n\nGood luck!"))
        self.game_text.grid(column = 0, row = 0, rowspan = 3, columnspan = 4)

        # State variables: coffee count, health, max health, location, lab equipment count
        self.coffee = 1
        self.health = 10
        self.max_health = 10
        self.strength = 4
        self.location = "Intro"
        self.equipment_count = 0

        # Buttons
        self.coffee_button = Button(main_container, text="DRINK COFFEE", state = DISABLED, command = self.drink_coffee, cursor = "coffee_mug")
        self.coffee_button.grid(column = 0, row = 4)
        self.seek_fight_button = Button(main_container, text="PICK A FIGHT", state = DISABLED, command = self.fight_setup, cursor = "hand2")
        self.seek_fight_button.grid(column = 1, row = 4)
        self.attack_button = Button(main_container, text = "ATTACK!", state = DISABLED, cursor = "hand2")
        self.attack_button.grid(column = 2, row = 4)
        self.run_away_button = Button(main_container, text="RUN AWAY!", state = DISABLED, cursor = "hand2")
        self.run_away_button.grid(column = 3, row = 4)

        # Health/Strength/Equipment Stats//Coffee count//Your location
        self.stats_frame = Frame(main_container, bg = "papaya whip")    # Sets frame to hold Stats
        self.stats_frame.grid(column = 4, row = 1, rowspan = 5)
        self.location_stats = Label(self.stats_frame, text = "Location: {}".format(self.location), bg = "papaya whip", font = ("Helvetica", 14))
        self.location_stats.grid(column = 4, row = 1)
        self.health_stats = Label(self.stats_frame, text = "Health: {}/{}".format(self.health, self.max_health),  bg = "papaya whip", font = ("Helvetica", 14))
        self.health_stats.grid(column = 4, row = 2)
        self.strength_stats = Label(self.stats_frame, text = "Strength: {}".format(self.strength), font = ("Helvetica", 14), bg = "papaya whip")
        self.strength_stats.grid(column = 4, row = 3)
        self.equipment_stats = Label(self.stats_frame, text = "Lab Equipment: {}/3".format(self.equipment_count), font = ("Helvetica", 14), bg = "papaya whip")
        self.equipment_stats.grid(column = 4, row = 4)
        self.coffee_count = Label(self.stats_frame, text = "Coffee: {}".format(self.coffee), bg = "papaya whip", font = ("Helvetica", 14))
        self.coffee_count.grid(column = 4, row = 5)

    # Figures out where user clicked, sends to correct land and/or gives unlock message
    def on_map_click(self, event):
        # user clicked The City
        if 28 <= event.x <= 128 and 88 <= event.y <= 200:
            self.enter_the_city(event)
        # player clicks the mountains, and has at least 1 piece of equipment
        elif 287 <= event.x <= 482 and 74 <= event.y <= 170 and self.equipment_count > 0:
            self.enter_the_mountains(event)
        # player clicks antarctica, code makes sure it's unlocked
        elif 53 <= event.x <= 175 and 235 <= event.y <= 342 and self.equipment_count > 1:
            self.enter_antarctica(event)
        # player clicks the lab, code makes sure it's unlocked
        elif 300 <= event.x <= 428 and 235 <= event.y <= 336 and self.equipment_count == 3:
            self.enter_the_lab(event)
        else:
            self.game_text.config(text = "That area isn't unlocked yet. Try picking a fight to find more lab equipment.")

    def enter_the_lab(self, event):
        # Changes game text
        self.game_text.config(text = (
            "You enter \"The Lab\"!\n\n"
            "Make sure to gather your health and strength before getting back to work..."
            ))
        self.location = "The Lab"
        self.location_stats.config(text = "Location: {}".format(self.location))

    def enter_antarctica(self, event):
        # Changes game text
        self.game_text.config(text = (
            "You enter \"Antarctica\"!\n\n"
            "From here you can heal your wounds with a cup of coffee,"
            "pick a fight with the locals,"
            "or go somewhere else on your map."
            ))
        self.location = "Antarctica"
        self.location_stats.config(text = "Location: {}".format(self.location))

    def enter_the_mountains(self, event):
        # Changes game text
        self.game_text.config(text = (
            "You enter \"The Mountains\"!\n\n"
            "From here you can heal your wounds with a cup of coffee,"
            "pick a fight with the locals,"
            "or go somewhere else on your map."
            ))
        self.location = "The Mountains"
        self.location_stats.config(text = "Location: {}".format(self.location))

    # User clicks in The City
    def enter_the_city(self, event):
        # Enables buttons on root window
        self.enable_buttons()
        # Changes game text
        self.game_text.config(text = (
            "You enter \"The City\"!\n\nA concrete realm of sunshine, adventure, and gentrification.\n\n"
            "From here you can heal your wounds with a cup of coffee,"
            "pick a fight with the locals,"
            "or go somewhere else on your map."
            ))
        self.location = "The City"
        self.location_stats.config(text = "Location: {}".format(self.location))

    # # Figures out where player clicks
    # def get_click(self, event):
    #     print("x-coordinate: {}, y-coordinate: {}".format(event.x, event.y))

    # Called during a fight to update health stats
    def fight_health_stats(self):
        self.health_stats.config(text = "Health: {}/{}".format(self.health, self.max_health))

    def disable_buttons(self):
        self.coffee_button.config(state = DISABLED)
        self.seek_fight_button.config(state = DISABLED)
        self.run_away_button.config(state = DISABLED)

    def enable_buttons(self):
        self.coffee_button.config(state = NORMAL)
        self.seek_fight_button.config(state = NORMAL)
        self.run_away_button.config(state = DISABLED)
        self.attack_button.config(state = DISABLED)

    def ignore(self, event):   # used to disable button click events
        pass

    # Checks location, populates enemies for that location
    def get_enemy(self):
        pick = random.randint(0,2)
        if self.location == "The City":  # total stats = 7
            if pick == 0:
                self.enemy = {
                    "name": "an Evil Landlord",
                    "attack phrase": "They pummel you with eviction notices.",
                    "strength": 2,
                    "health": 5}
            if pick == 1:
                self.enemy = {
                    "name": "a Pizza Rat",
                    "attack phrase": "They attack you with clever memes.",
                    "strength": 3,
                    "health": 4}
            else:
                self.enemy = {
                    "name": "bedbugs",
                    "attack phrase": "Did you know that bedbugs can survive for months without food or water?",
                    "strength": 1,
                    "health": 6}
        elif self.location == "The Mountains": # total stats = 14
            if pick == 0:
                self.enemy = {
                    "name": "giant spiders",
                    "attack phrase": "You try to explain the difference between venomous and poisonous, but they bite you anyway.",
                    "strength": 5,
                    "health": 8}
            if pick == 1:
                self.enemy = {
                    "name": "a walking tree",
                    "attack phrase": "It deftly ignores its lack of flexible cell walls.",
                    "strength": 7,
                    "health": 7}
            else:
                self.enemy = {
                    "name": "Bigfoot",
                    "attack phrase": "He disproves his existance while making you regret yours.",
                    "strength": 6,
                    "health": 9}
        elif self.location == "Antarctica":  # total stats = 30
            if pick == 0:
                self.enemy = {
                    "name": "a polar bear",
                    "attack phrase": "Climate change must be getting pretty bad to find polar bears in Antarctica!",
                    "strength": 16,
                    "health": 14}
            if pick == 1:
                self.enemy = {
                    "name": "rabid penguins", "attack phrase": "They just look so adorable as they try to peck your eyes out.",
                    "strength": 14 , "health": 16}
            else:
                self.enemy = {
                    "name": "rougue astronomers", "attack phrase": "They've had nothing but ramen for weeks, so they're pretty grumpy.",
                    "strength": 15, "health": 15}
        else:     # total stats = 50
            if pick == 0:
                self.enemy = {
                    "name": "the replicability crisis",
                    "attack phrase": "Do we even know anything?!",
                    "strength": 30,
                    "health": 20}
            if pick == 1:
                self.enemy = {
                    "name": "science denialists",
                    "attack phrase": "They hit you with homeopathic weapons, which do no damage. Unfortunately, science denialism causes real, widespread harm.",
                    "strength": 25 ,
                    "health": 25}
            else:
                self.enemy = {
                    "name": "a giant pile of unorganized data",
                    "attack phrase": "These columns and rows just make no sense.",
                    "strength": 20,
                    "health": 30}
        return self.enemy

    # Gets enemies, diables buttons on root window, enables Run Away and Attack! buttons
    def fight_setup(self):
        self.disable_buttons()
        self.attack_button.config(state = NORMAL)
        self.enemy = self.get_enemy()
        # Encounter an ememy
        self.fight_text = "You encounter {}.\n\n They have {} strength and {} health.\n\n".format(self.enemy["name"], self.enemy["strength"], self.enemy["health"])
        self.game_text.config(text = self.fight_text)
        self.attack_button.bind("<Button-1>", self.attack)
        # Deals with run away button during fight
        self.run_away_button.config(state = NORMAL)  # If clicked, should return player to main location text
        if self.location == "The City":
            self.run_away_button.bind("<Button-1>", self.enter_the_city)
        elif self.location == "The Mountains":
            self.run_away_button.bind("<Button-1>", self.enter_the_mountains)
        elif self.location == "Antarctica":
            self.run_away_button.bind("<Button-1>", self.enter_antarctica)
        elif self.location == "The Lab":
            self.run_away_button.bind("<Button-1>", self.enter_the_lab)

    # Handles the logic of fights when player presses Attack button
    def attack(self, event):
        # Decides whether you attack first or the enemy gets the jump on you
        attack_first = random.randint(0,1)
        if attack_first == 0:
            who_attacks_first = "You attack them with your lightning fast reflexes.\n\nThey lose {} health.".format(self.strength)
            self.enemy["health"] -= self.strength
        else:
            who_attacks_first = "{}\n\nYou lose {} health.".format(self.enemy["attack phrase"], self.enemy["strength"])
            # Checks to see how much health you have (you can't go less than 0)
            if self.health > self.enemy["strength"]:
                self.health -= self.enemy["strength"]
            # Makes sure player health can't go less than 0
            else:
                self.health = 0
            self.fight_health_stats()

        # Checks to see if player won fight, runs get lot funciton and outputs loot won
        if self.enemy["health"] <= 0:
            loot = self.get_loot()
            self.game_text.config(text = "{}\n\nYou win! You get {}".format(who_attacks_first, loot))
            self.enable_buttons()
            self.attack_button.bind("<Button-1>", self.ignore)   # makes it so you can't click attack button
            self.run_away_button.bind("<Button-1>", self.ignore)

        # Checks to see if player lost game
        elif self.health < 1:
            self.game_text.config(text = "GAME OVER.\n\nYou lose the game. Try again from the beginning."
            "And remember, in science, everyone wins when we learn. Except you. You still lose. Sorry.")
            self.end_game()

        #Updates fight text
        else:
            self.game_text.config(text = who_attacks_first)

    def add_special_item(self, special_item):
        self.equipment_count += 1
        self.equipment_stats.config(text = "Lab Equipment: {}/3".format(self.equipment_count))
        self.loot.append(special_item)

    # Deals with the logic of loot drops
    def get_loot(self):
        self.loot = []
        # Checks if you need to win a piece of lab equipment; probablility 1:6
        if random.randint(0,5) == 0:
            if self.location == "The City" and self.equipment_count < 1:
                special_item = "an Electrostatic Analyzer!\nThe Mountains are unlocked."
                self.add_special_item(special_item)
                self.map_label.config(image = self.map_image2)                      # updates map image to add mountains
            elif self.location == "The Mountains" and self.equipment_count < 2:
                special_item = "a tank of Supercooled Helium!\nAntarctica is now unlocked."
                self.add_special_item(special_item)
                self.map_label.config(image = self.map_image3)                      #  updates map image to add Antarctica
            elif self.location == "Antarctica" and self.equipment_count < 3:
                special_item = "a Cold Laser!\nThe Lab is unlocked."
                self.add_special_item(special_item)
                self.map_label.config(image = self.map_image4)             # updates map to add The Lab
            elif self.location == "The Lab":
                special_item = ("A Nobel prize!!!! You win!!!!\n\nJust kidding.\n"
                "In all likelihood you won't be recognized for your years of hard work and tireless study for very little pay.\n\n"
                "But you did win the game! Congratulations!")
                self.loot.append(special_item)
                self.end_game()
            else:
                pass

        # Checks if you win coffee; probablility 1:3
        if random.randint(0,2) == 0:
            self.loot.append("a cup of coffee.")
            self.coffee += 1
            self.coffee_count.config(text = "Coffee: {}".format(self.coffee))

        # Data structures to hold possible max health and strength loot
        possible_loot = {
            "health item": [
                "safety goggles. You feel much safer.\nYour max health increases.",
                "a pocket protector. You're not sure what this does, but you feel much safer anyway.\n\nYour max health increases.",
                "a kevlar lab coat. Once you figure out how to walk in this thing you're going to be unstoppable.\n\nYour max health increases.",
                "rubber gloves.\n\nYour max health increases as your dexterity decreases."
                "a bottle of deionized water. As long as you remember to add it before the acid, you'll be fine.\n\nYour max health increases."
            ],
            "strength item": [
                "a basic sword. It's not a very good sword, but it is heavy.\n\nAfter carrying it for awhile you feel much stronger!",
                "a robotic dog, an engineer's best friend.\n\nYour strength increases with its presence.",
                "a robotic cat. It won't do what you tell it to do, but it has vicious claws.\n\nYour strength increases.",
                "a gold-plated pipette. Good for poking enemies in the eye and not much else.\n\nYour strength increases."
                "a pen. It's fairly mighty, but you decide to hang onto your sword just in case.\n\nYour strength increases."
            ]
        }

        # Picks a random health item, checks if you win it, updates max health stats; probability 1:4
        if random.randint(0,3) == 0:
            self.loot.append("\nYou also win {}".format(random.choice(possible_loot["health item"])))
            self.max_health += 2
            self.health_stats.config(text = "Health: {}/{}".format(self.health, self.max_health))

        # Picks a random health item, checks if you win it, updates max health stats; probability 1:4
        if random.randint(0,3) == 0:
            self.loot.append(random.choice(possible_loot["strength item"]))
            self.strength += 2
            self.strength_stats.config(text = "Strength: {}".format(self.strength))

        # Gets a long string with all loot aquired
        loot_string = ""
        for i in range(len(loot)):
            if i == 0:
                loot_string += "{}\n".format(loot[i])
            else:
                loot_string += "\nYou also won {}".format(loot[i])
        # Makes sure player doesn't get an empty string
        if loot_string == "":
            loot_string = "nothing."
        return loot_string

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

    # Used to end the game functionality (takes no input)
    def end_game(self):
        self.disable_buttons()
        self.run_away_button.config(state = DISABLED)
        self.attack_button.config(state = DISABLED)
        self.map_label.bind("<Button-1>", self.ignore)
        self.attack_button.bind("<Button-1>", self.ignore)   # makes it so you can't click any buttons
        self.run_away_button.bind("<Button-1>", self.ignore)

def main():
    root = Tk() # Creating a window object called root
    game = Game(root)
    root.mainloop() # Starts Tk program gameloop -- now

main()
