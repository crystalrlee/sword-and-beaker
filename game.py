# game.py
# Sword & Beaker adventure game

from tkinter import *

# Sets image for character
def get_avatar_image(root):
    avatar_image = PhotoImage(file = "warrior_girl.gif")
    label_avatar = Label(root, image = avatar_image)
    # Make sure photo piggybacks on label so it doesn't get garbage collected
    label_avatar.avatar_image = avatar_image
    label_avatar.pack(side = "left")
    return label_avatar

# Sets input field for users to enter text
def get_input_text_field(root):
    input_text_field = Entry(root)
    input_text_field.pack()
    return input_text_field

# Sets field where users will see main output of game (text area for fights, directions, etc.)
def get_game_text(root):
    game_text = Label(root, text = "Testing... how much text can go here?",
        fg = "green2", bg = "grey1", height = "40", width = "80" )
    game_text.pack()
    return game_text

# Sets submit button for text input field
def get_submit_button(root):
    submit_button = Button(root, text="Submit")
    submit_button.pack()
    return submit_button

# Sets label for player health stats
def get_health_stats(root):
    health_stats = Label(root, text = "Health: 5/5")
    health_stats.pack(side = "left")
    return health_stats

def get_strength_stats(root):
    strength_stats = Label(root, text = "Strength: 4/4")
    strength_stats.pack(side = "left")
    return strength_stats

def get_moxie_stats(root):
    moxie_stats = Label(root, text = "Moxie: 4/4")
    moxie_stats.pack(side = "left")
    return moxie_stats

# Checks how many scuba suit pieces player has
def get_scuba_stats(root):
    scuba_stats = Label(root, text = "Scuba suit: 0/3")
    scuba_stats.pack(side = "left")
    return scuba_stats

def main():
    # Creates the main tk window object, called "root" by convention. (Window where the game happens.)
    root = Tk()
    root.title("Sword & Beaker")
    root.geometry("1100x650")
    root.configure(background = "white")

    # loads avatar image
    avatar_image = get_avatar_image(root)

    #loads game text and input text field and submit button
    game_text = get_game_text(root)
    input_text_field = get_input_text_field(root)
    submit_button = get_submit_button(root)

    # loads stat labels
    health_stats = get_health_stats(root)
    strength_stats = get_strength_stats(root)
    moxie_stats = get_moxie_stats(root)
    scuba_stats = get_scuba_stats(root)

    # opens the main game window, called "root"
    root.mainloop()

main()
