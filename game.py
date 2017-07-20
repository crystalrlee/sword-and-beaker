# game.py
# Sword & Beaker adventure game

from tkinter import *

# Creates main container frame
def get_main_container(root):
    main_container = Frame(root)
    main_container.grid()
    main_container.configure(bg = "white")
    return main_container

# Sets image for character
def get_avatar_image(main_container):
    avatar_image = PhotoImage(file = "warrior_girl.gif")
    label_avatar = Label(main_container, image = avatar_image, bd = 10)
    # Make sure photo piggybacks on label so it doesn't get garbage collected
    label_avatar.avatar_image = avatar_image
    label_avatar.grid(column = 0, row = 0)
    return label_avatar

# Sets field where users will see main output of game (text area for fights, directions, etc.)
def get_game_text(main_container):
    game_text = Label(main_container, text = "Testing... how much text can go here?",
        fg = "green2", bg = "grey1", height = "30", width = "92")
    game_text.grid(column = 1, row = 0, columnspan = 4)
    return game_text

# Sets map button
def get_map_button(main_container):
    map_button = Button(main_container, text="MAP")
    map_button.grid(column = 1, row = 2)
    return map_button

# Sets inventory button
def get_inventory_button(main_container):
    inventory_button = Button(main_container, text="INVENTORY")
    inventory_button.grid(column = 2, row = 2)
    return inventory_button

# Sets attack button
def get_attack_button(main_container):
    attack_button = Button(main_container, text="ATTACK!")
    attack_button.grid(column = 3, row = 2)
    return attack_button

# Sets run away button
def get_run_away_button(main_container):
    run_away_button = Button(main_container, text="RUN AWAY!")
    run_away_button.grid(column = 4, row = 2)
    return run_away_button

# Sets label for player health stats
def get_health_stats(main_container):
    health_stats = Label(main_container, text = "Health: 5/5",  bg = "white", font = ("Helvetica", 14))
    health_stats.grid(column = 0, row = 1)
    return health_stats

def get_strength_stats(main_container):
    strength_stats = Label(main_container, text = "Strength: 4/4", font = ("Helvetica", 14), bg = "white")
    strength_stats.grid(column = 0, row = 2)
    return strength_stats

# Checks how many scuba suit pieces player has
def get_lab_equipment_stats(main_container):
    lab_equipment_stats = Label(main_container, text = "Lab Equipment: 0/3", font = ("Helvetica", 14), bg = "white")
    lab_equipment_stats.grid(column = 0, row = 4)
    return lab_equipment_stats

def main():
    # Creates the main tk window object, called "root" by convention.
    root = Tk()
    root.title("Sword & Beaker")
    root.geometry("1100x570")
    root.configure(background = "white")

    # Calls main container frame
    main_container = get_main_container(root)

    # loads avatar image
    avatar_image = get_avatar_image(main_container)

    #loads game text and map button
    game_text = get_game_text(main_container)

    # loads game play buttons
    map_button = get_map_button(main_container)
    inventory_button = get_inventory_button(main_container)
    attack_button = get_attack_button(main_container)
    run_away_button = get_run_away_button(main_container)

    # loads stat labels
    health_stats = get_health_stats(main_container)
    strength_stats = get_strength_stats(main_container)
    lab_equpiment_stats = get_lab_equipment_stats(main_container)

    # opens the main game window, called "root"
    root.mainloop()

main()
