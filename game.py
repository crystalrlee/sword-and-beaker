# game.py
# Sword & Beaker adventure game

import tkinter

# Sets image for character
def get_avatar_image(window):
    avatar_image = tkinter.PhotoImage(file = "warrior_girl.gif")
    label_avatar = tkinter.Label(window, image = avatar_image)
    # Make sure photo piggybacks on label so it doesn't get garbage collected
    label_avatar.avatar_image = avatar_image
    label_avatar.pack(side = "left")
    return label_avatar

def main():
    # creates a tk window object
    window = tkinter.Tk()
    window.title("Sword & Beaker")
    window.geometry("1400x800")

    # loads avatar image
    avatar_image = get_avatar_image(window)


    # opens the window
    window.mainloop()



main()
