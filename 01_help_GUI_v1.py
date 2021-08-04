"""
The first version of a help GUI. This program creates a frame for the help button
Created on 27/07/21 by Ashlee Barrell
"""

from tkinter import *


class Results:
    def __init__(self):

        # Formatting variables
        background_colour = "Light blue"

        # Converter main screen GUI
        self.results_frame = Frame(width=300, height=300, bg=background_colour)
        self.results_frame.grid()

        # Temperature Conversion Heading (row 0)
        self.race_results_label = Label(text="Race Results",
                                        font=("Arial", "16", "bold"),
                                        bg=background_colour,
                                        padx=10, pady=10)
        self.race_results_label.grid(row=0)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Sports Analysis Program")
    something = Results()
    root.mainloop()
