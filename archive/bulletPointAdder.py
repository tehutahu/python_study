#! python3
# bulletPointAdder.py
# Get strings splited by \n from clipbode and return them with '*' to clipbode

import sys
import pyperclip

# get text from clipbode
text = pyperclip.paste()

# set '*' in front of each text
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]
text = '\n'.join(lines)

# return text to clipbode
pyperclip.copy(text)
