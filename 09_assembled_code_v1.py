from tkinter import *
from functools import partial  # To prevent unwanted windows
from tkinter import messagebox
import re


class Results:
    def __init__(self):
        # Formatting variables
        background_colour = "Light blue"

        self.result_list = []

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

        # Button that allows user to input a new  participant
        self.next_participant = Button(self.results_frame,
                                       text="Next participant",
                                       width=15,
                                       font="Arial 12 bold",
                                       command=self.participant)
        self.next_participant.grid(row=5, pady=10)

        # History/Help button frame (row 6)
        self.hist_help_frame = Frame(self.results_frame, bg=background_colour)
        self.hist_help_frame.grid(row=6, column=0, pady=10)

        self.result_hist_button = Button(self.hist_help_frame,
                                         font="Arial 12 bold",
                                         text="History",
                                         command=lambda: self.history(self.result_list),
                                         width=5,
                                         justify=CENTER)
        self.result_hist_button.grid(row=0, column=0, sticky=W)

        if len(self.result_list) == 0:
            self.result_hist_button.config(state=DISABLED)

        self.help_button = Button(self.hist_help_frame, font="Arial 12 bold",
                                  text="Help", width=5, justify=CENTER)
        self.help_button.grid(row=0, column=1, padx=10)

    # Check for valid string
    def string_checker(self, test):
        while True:
            to_test = test
            if to_test.isdigit():
                return True
            else:
                return False

    def participant(self):
        result = self.results_entry.get()
        error = "Invalid entry. Must be a name followed by time greater than 0"
        result.strip()
        result = result.split()

        if len(result) < 2:
            messagebox.showerror("Error", error)

        elif result[1][0].isdigit():
            time = float(result[1])
            if time < 1:
                messagebox.showerror("Error", error)

            elif result[0].isdigit():
                messagebox.showerror("Error", error)

            else:
                name = result[0]
                self.result_list.append([time, name])
                self.results_entry.delete(0, END)
                # display answer

        else:
            messagebox.showerror("Error", error)

        # Checks the number of appended items in the list and gives error if 0
        if len(self.result_list) == 0:
            error = "The list of participants is empty. Please enter participants."
            messagebox.showerror("Error", error)
            self.result_hist_button.config(state=DISABLED)
        else:
            self.result_hist_button.config(state=ACTIVE)

    def history(self, result_list):
        History(self, result_list)


class Help:
    def __init__(self, partner):
        background = "orange"

        # Disable help button
        partner.help_button.config(state=DISABLED)
        # sets up child window (ie: help box)
        self.help_box = Toplevel()

        # If users press cross at top, closes help and 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help,
                                                           partner))

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
                                  command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        # Puts the help button back to normal
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


class History:
    def __init__(self, partner, result_list):
        background = "#a9ef99"  # Pale green

        # Disable history button
        partner.result_hist_button.config(state=DISABLED)
        # sets up child window (ie: history box)
        self.history_box = Toplevel()

        # If users press cross at top, closes history and 'releases' history button
        self.history_box.protocol('WM_DELETE_WINDOW', partial(self.close_history,
                                                              partner))

        # set up GUI Frame
        self.history_frame = Frame(self.history_box, width=300, bg=background)
        self.history_frame.grid()

        # Set up history heading
        self.how_heading = Label(self.history_frame, text="Race History",
                                 font="ariel 10 bold", bg=background)
        self.how_heading.grid(row=0)

        # history text (label, row 1)
        self.history_text = Label(self.history_frame,
                                  text="Here are the most recent entries. "
                                       "Use the export button to create a text file "
                                       "of all your participants in order of fastest to slowest times",
                                  font="arial 10 italic", wrap=250,
                                  justify=LEFT, fg="maroon",
                                  width=40, bg=background)
        self.history_text.grid(row=1)

        # History output (row 2)
        history_string = ""
        max_length = 5
        if len(result_list) >= max_length:
            for index in range(len(result_list) - 1, (len(result_list) - max_length) - 1, -1):
                history_string += result_list[index][1] + " : " + str(result_list[index][0]) + "\n"
        else:
            for item in result_list:
                history_string += item[1].title() + " : " + str(item[0]) + "\n"

                self.history_text.config(text="Your result history."
                                              "You can use the export button to save "
                                              "data to a text file if desired.")

        # label to display result history
        self.hist_label = Label(self.history_frame, text=history_string,
                                bg=background, font="Arial 12", justify=LEFT)
        self.hist_label.grid(row=2)

        # Export frame row 3
        self.export_dismiss_frame = Frame(self.history_frame)
        self.export_dismiss_frame.grid(row=3, pady=10)

        # Export button
        self.export_button = Button(self.export_dismiss_frame, text="Export",
                                    font="arial 12 bold", command=lambda: self.export(result_list))
        self.export_button.grid(row=0, column=0)

        # Dismiss Button
        self.dismiss_button = Button(self.export_dismiss_frame, text="Dismiss",
                                     font="arial 12 bold",
                                     command=partial(self.close_history, partner))
        self.dismiss_button.grid(row=0, column=1)

    def close_history(self, partner):
        # Puts the history button back to normal
        partner.result_hist_button.config(state=NORMAL)
        self.history_box.destroy()

    def export(self, result_list):
        Export(self, result_list)


class Export:
    def __init__(self, partner, result_list):
        background = "#a9ef99"  # Pale Green

        # Disable export button
        partner.export_button.config(state=DISABLED)
        # sets up child window (ie: export box)
        self.export_box = Toplevel()

        # If users press cross at top, closes export dialogue and 'releases' export button
        self.export_box.protocol('WM_DELETE_WINDOW', partial(self.close_export,
                                                             partner))

        # set up GUI Frame
        self.export_frame = Frame(self.export_box, width=300, bg=background)
        self.export_frame.grid()

        # Set up export heading
        self.how_heading = Label(self.export_frame, text="Export Instructions",
                                 font="ariel 10 bold", bg=background)
        self.how_heading.grid(row=0)

        # Export text (label, row 1)
        self.export_text = Label(self.export_frame,
                                 text="Enter a filename in the box."
                                      "Press the save button to save",
                                 justify=LEFT,
                                 width=40, bg=background, wrap=250)
        self.export_text.grid(row=1)

        # Warning text (label, row 2)
        self.export_text = Label(self.export_frame,
                                 text="If filename already exists it will be replaced.",
                                 justify=LEFT,
                                 bg="#ffafaf", fg="maroon",
                                 font="Arial 10 italic",
                                 pady=10, padx=10, wrap=250)
        self.export_text.grid(row=2, pady=10)

        # Filename entry box row 3
        self.filename_entry = Entry(self.export_frame, width=20,
                                    font="Arial 14 bold", justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)

        # Error message labels (row 4)
        self.save_error_label = Label(self.export_frame, text="", fg="maroon",
                                      bg=background)
        self.save_error_label.grid(row=4)

        # Save or cancel frame row 5
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=4, pady=10)

        # Save and cancel buttons row 0 of save cancel frame
        self.save_button = Button(self.save_cancel_frame, text="Save",
                                  command=partial(lambda: self.save_history(partner, result_list)))
        self.save_button.grid(row=0, column=0)

        self.cancel_button = Button(self.save_cancel_frame, text="Cancel",
                                    command=partial(self.close_export, partner))
        self.cancel_button.grid(row=0, column=1)

    def save_history(self, partner, result_list):
        filename = self.filename_entry.get()
        has_error = "no"

        valid_file = "[A-Za-z0-9]"
        for letter in filename:
            if re.match(valid_file, letter):
                continue

            elif letter == " ":
                problem = "(no spaces allowed)"

            else:
                problem = ("(no {}'s allowed)".format(letter))
            has_error = "yes"

        if filename == "":
            problem = "can't be blank"
            has_error = "yes"

        if has_error == "yes":
            messagebox.showerror("Error", problem)
        else:
            result_list.sort()
            # Add .txt suffix
            filename = filename + ".txt"

            # Creates file to hold data
            f = open(filename, "w+")

            f.write("100m Race\n")
            for element in result_list:
                f.write(f"{(result_list.index(element) + 1)} Name: {element[1].title()} - Time: {element[0]} seconds\n")

            # Close file
            f.close()
            self.close_export(partner)

    def close_export(self, partner):
        # Puts the export button back to normal
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Sports Analysis Program")
    something = Results()
    root.mainloop()
