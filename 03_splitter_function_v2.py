"""Further version of splitter function which splits the participants
from one line of input into name and time
Version 3 - testing on full participant list
Created by Ashlee Barrell
02/08/2021
"""

import re  # This is the Regular Expression module

# Reading from a full list of participants
# Participant list has name and time
full_participants = [
    "jade 5.20",
    "harry 4.40",
    "jack 4:20",
    "gwen 5:00"
]
# print (full_participants)
for participant in full_participants:
    participant_line = participant.strip()
    participant_entry = re.split("\s", participant_line, 1)
    print(f"Name: {participant_entry[0]}\nTime: {participant_entry[1]}\n".title())
