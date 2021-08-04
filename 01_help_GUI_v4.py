"""
The forth version of a help GUI. This program prevents unwanted windows by disabling the help button.
Created on 27/07/21 by Ashlee Barrell
"""

from tkinter import *
from functools import partial  # To prevent unwanted windows


class Results:
    def __init__(self):
        # Formatting variables
        background_colour = "Light blue"

        # Converter main screen GUI
        self.results_frame = Frame(width=300, height=300,
                                   bg=background_colour, pady=10)
        self.results_frame.grid()

        # Temperature Conversion Heading (row 0)
        self.race_results_label = Label(self.results_frame,
                                        text="Race Results",
                                        font=("Arial", "16", "bold"),
                                        bg=background_colour,
                                        padx=10, pady=10)
        self.race_results_label.grid(row=0)

        # Help button (row 1)
        self.help_button = Button(self.results_frame, text="Help",
                                  font=("Arial", "14"),
                                  padx=10, pady=10,
                                  command=self.help)
        self.help_button.grid(row=1)

    def help(self):
        get_help = Help(self)
        get_help.help_text.configure(text="Help text goes here")


class Help:
    def __init__(self, partner):
        background = "orange"

        # Disable help button
        partner.help_button.config(state=DISABLED)
        # sets up child window (ie: help box)
        self.help_box = Toplevel()

        # set up GUI Frame
        self.help_frame = Frame(self.help_box, width=300, bg=background)
        self.help_frame.grid()

        # Set up help heading
        self.how_heading = Label(self.help_frame, text="Help/Instructions",
                                 font="ariel 10 bold", bg=background)
        self.how_heading.grid(row=0)

        # Help text (label, row 1)
        self.help_text = Label(self.help_frame, text="", justify=LEFT,
                               width=40, bg=background, wrap=250)
        self.help_text.grid(row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss",
                                  width=10, bg="orange", font="arial 10 bold",
                                  command=self.close_help)
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self):
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Sports Analysis Program")
    something = Results()
    root.mainloop()
