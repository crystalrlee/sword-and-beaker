# game.py
# Sword & Beaker adventure game

from tkinter import *

# Creates main container frame
def get_main_container(root):
    main_container = Frame(root)
    main_container.pack()
    main_container.configure(bg = "white")
    return main_container

# Sets image for character
def get_avatar_image(main_container):
    avatar_image = PhotoImage(file = "warrior_girl.gif")
    label_avatar = Label(main_container, image = avatar_image)
    # Make sure photo piggybacks on label so it doesn't get garbage collected
    label_avatar.avatar_image = avatar_image
    label_avatar.pack(side = "left")
    return label_avatar

# Sets input field for users to enter text
def get_input_text_field(main_container):
    input_text_field = Entry(main_container)
    input_text_field.pack()
    return input_text_field

# Sets field where users will see main output of game (text area for fights, directions, etc.)
def get_game_text(main_container):
    game_text = Label(main_container, text = "Testing... how much text can go here?",
        fg = "green2", bg = "grey1", height = "40", width = "80" )
    game_text.pack()
    return game_text

# Sets submit button for text input field
def get_submit_button(main_container):
    submit_button = Button(main_container, text="Submit")
    submit_button.pack()
    return submit_button

# Sets label for player health stats
def get_health_stats(main_container):
    health_stats = Label(main_container, text = "Health: 5/5")
    health_stats.pack(side = "left")
    return health_stats

def get_strength_stats(main_container):
    strength_stats = Label(main_container, text = "Strength: 4/4")
    strength_stats.pack(side = "left")
    return strength_stats

def get_moxie_stats(main_container):
    moxie_stats = Label(main_container, text = "Moxie: 4/4")
    moxie_stats.pack(side = "left")
    return moxie_stats

# Checks how many scuba suit pieces player has
def get_scuba_stats(main_container):
    scuba_stats = Label(main_container, text = "Scuba suit: 0/3")
    scuba_stats.pack(side = "left")
    return scuba_stats

def main():
    # Creates the main tk window object, called "root" by convention.
    root = Tk()
    root.title("Sword & Beaker")
    root.geometry("1100x650")
    root.configure(background = "white")

    # Calls main container frame
    main_container = get_main_container(root)

    # loads avatar image
    avatar_image = get_avatar_image(main_container)

    #loads game text and input text field and submit button
    game_text = get_game_text(main_container)
    input_text_field = get_input_text_field(main_container)
    submit_button = get_submit_button(main_container)

    # loads stat labels
    health_stats = get_health_stats(main_container)
    strength_stats = get_strength_stats(main_container)
    moxie_stats = get_moxie_stats(main_container)
    scuba_stats = get_scuba_stats(main_container)

    # opens the main game window, called "root"
    root.mainloop()

main()
