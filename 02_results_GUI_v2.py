"""Results GUI v2
Basic tkinter template
This program adds the necessary features
created by Ashlee Barrell 28/07/21
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

        # User instructions row 1
        self.entry_instructions_label = Label(self.results_frame,
                                              text="Please enter the race length in meters in the first box"
                                                   " and the participant's name and time in the second.",
                                              font="Arial 10 italic", wrap=250,
                                              justify=LEFT, bg=background_colour,
                                              padx=10, pady=10)
        self.entry_instructions_label.grid(row=1)

        # Race length entry box row 2
        entry_box = Entry(self.results_frame)
        entry_box.grid(row=2, column=0, padx=5, pady=10)
        race_length = entry_box.get()
        print(race_length)

        # Format instructions for result entry row 3
        self.format_instructions_label = Label(self.results_frame,
                                               text="When entering the times please format it like this:\n"
                                                    "participant's name <SPACE> time taken.",
                                               font="Arial 10 italic", wrap=250,
                                               justify=LEFT, bg=background_colour,
                                               padx=10, pady=10)
        self.format_instructions_label.grid(row=3)

        # Results entry box row 4
        self.results_entry = Entry(self.results_frame, width=20,
                                   font="Arial 14 bold")
        self.results_entry.grid(row=4)

        # Last inputted name and time label row 5
        self.last_entry_label = Label(self.results_frame,
                                      font="Arial 14 bold",
                                      fg="purple", bg=background_colour,
                                      pady=10, text="Last entry goes here")
        self.last_entry_label.grid(row=5)

        # History/Help button frame (row 6)
        self.hist_help_frame = Frame(self.results_frame)
        self.hist_help_frame.grid(row=6, pady=10)

        self.result_hist_button = Button(self.hist_help_frame,
                                         font="Arial 12 bold",
                                         text="History",
                                         width=5)
        self.result_hist_button.grid(row=0, column=0)

        self.help_button = Button(self.hist_help_frame, font="Arial 12 bold",
                                  text="Help", width=5)
        self.help_button.grid(row=0, column=1)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Sports Analysis Program")
    something = Results()
    root.mainloop()
