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

        # Export button (row 1)
        self.export_button = Button(self.results_frame, text="Export",
                                    font=("Arial", "14"),
                                    padx=10, pady=10,
                                    command=self.export)
        self.export_button.grid(row=1)

    def export(self):
        get_export = Export(self)


class Export:
    def __init__(self, partner):
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
        self.export_text.grid(row=2)

        # Filename entry box row 3
        self.filename_entry = Entry(self.export_frame, width=20,
                                    font="Arial 14 bold", justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)

        # Save or cancel frame row 4
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=4, pady=10)

        # Save and cancel buttons row 0 of save cancel frame
        self.save_button = Button(self.save_cancel_frame, text="Save")
        self.save_button.grid(row=0, column=0)

        self.cancel_button = Button(self.close_export, text="Cancel")
        self.cancel_button.grid(row=0, column=1)

    def close_export(self, partner):
        # Puts the export button back to normal
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()
