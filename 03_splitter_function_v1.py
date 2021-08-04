"""Initial version of an item splitter which splits the participant's name and time
Version 1 - this version tells the user if the regex follows the written formula
Allows both . and : symbols for time.
Created by Ashlee Barrell
29/07/2021
"""

import re  # This is the Regular Expression module

# Line has both name and time in it and will be split so it it name and time
name_and_time = "jay 5:30"  # Change to input statement in due course


# The regex format below is expecting: number <space> number
mixed_regex = "[a-z]{1,}\s\d{1,3}[.:]\d{1,2}"
# \d for a digit, /d{1,3] allows 1-3 digits, /s for space, [a-z] for letters, {1,} means at least one letter,
# but can be limited

# Testing to see if the recipe line matches the regular expression
if re.match(mixed_regex, name_and_time):
    print("True")
else:
    print("False")
