# Problem
# Text Alignment Functions in Python

This repository contains Python functions to align text within a specified width. The alignment styles include:

- Left
- Right
- Center
- Justify

## Functions

### 1. `left_align`

#### Purpose

To split a given text into lines such that each line is left-aligned and does not exceed a specified width.

#### Code

```python
def left_align(text, width):
    words = text.split()  # Split the text into individual words.
    lines = []  # Initialize an empty list to store the lines.
    current_line = ""  # Initialize an empty string to store the current line.

    for word in words:  # Loop through each word in the text.
        if len(current_line) + len(word) + 1 <= width:  # Check if adding the word exceeds the width.
            if current_line:  # If current_line is not empty, add a space before the word.
                current_line += " " + word
            else:  # If current_line is empty, start it with the word.
                current_line = word
        else:  # If adding the word exceeds the width, finalize the current line.
            lines.append(current_line)  # Append the current line to the lines list.
            current_line = word  # Start a new line with the current word.

    if current_line:  # Append the last line if it exists.
        lines.append(current_line)

    return lines  # Return the list of left-aligned lines.
