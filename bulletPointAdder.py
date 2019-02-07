#! python3
# bulletPointAdder.py - add bullet points to lines

import pyperclip

text = pyperclip.paste()

# seperate lines
lines = text.split('\n')

# add *(star) to each line
for i in range(len(lines)):
	lines[i] = '* ' + lines[i]

# join lines
text = '\n'.join(lines)

pyperclip.copy(text)
