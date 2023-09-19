import pyautogui
import time

# Data to type, separated by newline characters
data_to_type = """24
11
60
68
65
66
7
74
85
77
80
85
94
43
26
28
60
29
79
70
91
65
40
21
"""

# Split the data into individual lines
lines = data_to_type.split('\n')

# Sleep for a few seconds to give you time to focus on the input field
time.sleep(5)

# Loop through each line and type it, then press the Tab key
for line in lines:
    pyautogui.typewrite(line)
    pyautogui.press('tab')
    #time.sleep(0.1)  # Add a small delay between entries (adjust as needed)

# Optionally, add a final "Enter" to submit the form
# pyautogui.press('enter')
