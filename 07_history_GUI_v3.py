from tkinter import *
from functools import partial  # To prevent unwanted windows


class Results:
    def __init__(self):
        # Formatting variables
        background_colour = "Light blue"

        self.result_list = ['4 Jay',
                            '3.7 Maebh',
                            '3.8 Luna',
                            '4.3 Ben',
                            '4.1 John']

        # Converter main screen GUI
        self.results_frame = Frame(width=300, height=300,
                                   bg=background_colour, pady=10)
        self.results_frame.grid()

        # Race Results Heading (row 0)
        self.race_results_label = Label(self.results_frame,
                                        text="Race Results",
                                        font=("Arial", "16", "bold"),
                                        bg=background_colour,
                                        padx=10, pady=10)
        self.race_results_label.grid(row=0)

        # history button (row 1)
        self.history_button = Button(self.results_frame, text="history",
                                     font=("Arial", "14"),
                                     padx=10, pady=10,
                                     command=lambda: self.history(self.result_list))
        self.history_button.grid(row=1)

    def history(self, calc_history):
        History(self, calc_history)


class History:
    def __init__(self, partner, result_list):
        background = "#a9ef99"  # Pale green

        # Disable history button
        partner.history_button.config(state=DISABLED)
        # sets up child window (ie: history box)
        self.history_box = Toplevel()

        # If users press cross at top, closes history and 'releases' history button
        self.history_box.protocol('WM_DELETE_WINDOW', partial(self.close_history,
                                                              partner))

        # set up GUI Frame
        self.history_frame = Frame(self.history_box, width=300, bg=background)
        self.history_frame.grid()

        # Set up history heading
        self.how_heading = Label(self.history_frame, text="Calculation History",
                                 font="ariel 10 bold", bg=background)
        self.how_heading.grid(row=0)

        # history text (label, row 1)
        self.history_text = Label(self.history_frame,
                                  text="Here are the most recent calculations,"
                                       "Use the export button to create a text file"
                                       "of all your calculations",
                                  font="arial 10 italic", wrap=250,
                                  justify=LEFT, fg="maroon",
                                  width=40, bg=background)
        self.history_text.grid(row=1)

        # History output (row 2)
        history_string = ""
        if len(result_list) >= 7:
            for item in range(0, 7):
                history_string += result_list[len(result_list) - item - 1] + "\n"

        else:
            for item in result_list:
                history_string += result_list[len(result_list) -
                                              result_list.index(item) - 1] + "\n"
                self.history_text.config(text="Your calculation history."
                                              "You can use the export button to save "
                                              "data to a text file if desired.")

        # label to display calculation history
        self.hist_label = Label(self.history_frame, text=history_string,
                                bg=background, font="Arial 12", justify=LEFT)
        self.hist_label.grid(row=2)

        # Export frame row 3
        self.export_dismiss_frame = Frame(self.history_frame)
        self.export_dismiss_frame.grid(row=3, pady=10)

        # Export button
        self.export_button = Button(self.export_dismiss_frame, text="Export",
                                    font="arial 12 bold")
        self.export_button.grid(row=0, column=0)

        # Dismiss Button
        self.dismiss_button = Button(self.export_dismiss_frame, text="Dismiss",
                                     font="arial 12 bold",
                                     command=partial(self.close_history, partner))
        self.dismiss_button.grid(row=0, column=1)

    def close_history(self, partner):
        # Puts the history button back to normal
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Race Analysis Program")
    something = Results()
    root.mainloop()
