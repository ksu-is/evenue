from tkinter import *


def entry():
    """Show a simple login dialog in a Toplevel window.

    This function can be safely imported without creating windows; calling
    it will open a Toplevel and return immediately.
    """
    win = Toplevel()
    win.title("Login")

    # Create a user input window inside the Toplevel
    ent = Entry(win, width=30)
    ent.pack(padx=10, pady=10)

    #Defines the function for the button on the screen
    def myClick():
        username = ent.get().title()
        hello = "Welcome " + username
        myLabel01 = Label(win, text=hello)
        myLabel01.pack()

    myButton00 = Button(win, text="Username", command=myClick)
    myButton00.pack(padx=10, pady=(0,10))