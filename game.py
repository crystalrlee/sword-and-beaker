# game.py
# Sword & Beaker adventure game

from tkinter import *

# Sets image for character
def get_avatar_image(window):
    avatar_image = PhotoImage(file = "warrior_girl.gif")
    label_avatar = Label(window, image = avatar_image)
    # Make sure photo piggybacks on label so it doesn't get garbage collected
    label_avatar.avatar_image = avatar_image
    label_avatar.pack(side = "left")
    return label_avatar

def get_input_text_field(window):
    input_text_field = Entry(window)
    input_text_field.pack()
    return input_text_field

def get_game_text(window):
    game_text = Label(window, text = "Testing... how much text can go here?",
        fg = "green2", bg = "grey1", height = "40", width = "80" )
    game_text.pack()
    return game_text

def get_submit_button(window):
    submit_button = Button(window, text="Submit", state = "disabled")
    submit_button.pack()
    return submit_button

def main():
    # creates a tk window object
    window = Tk()
    window.title("Sword & Beaker")
    window.geometry("1400x800")

    # loads avatar image
    avatar_image = get_avatar_image(window)

    #loads game text and input text field and submit button
    game_text = get_game_text(window)
    input_text_field = get_input_text_field(window)
    submit_button = get_submit_button(window)

    # opens the window
    window.mainloop()

main()
