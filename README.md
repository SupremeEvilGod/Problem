# Problem

# Text Alignment Functions in Python

This repository contains Python functions to align text within a specified width. The alignment styles include:

- Left
- Right
- Center
- Justify

## Functions

### 1. `left_align`

#### Purpose:

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
```

### 2. `right_align`

#### Purpose:

To right-align text within a specified width.

#### Code

```python
def right_align(text, width):
    lines = left_align(text, width)  # First, get the left-aligned lines.
    for i in range(len(lines)):  # Loop through each line.
        lines[i] = lines[i].rjust(width)  # Right-align each line using the `rjust` method.
    return lines  # Return the list of right-aligned lines.
```

### 3. `center_align`
#### Purpose:

To center-align text within a specified width.

#### Code

```python
def center_align(text, width):
    lines = left_align(text, width)  # First, get the left-aligned lines.
    for i in range(len(lines)):  # Loop through each line.
        lines[i] = lines[i].center(width)  # Center-align each line using the `center` method.
    return lines  # Return the list of center-aligned lines.
```

### 4. `justify_align`
#### Purpose:
To justify-align text within a specified width, meaning the text is spread out so that each line (except the last) is exactly the specified width.

#### Code

```python

def justify_align(text, width):
    words = text.split()  # Split the text into individual words.
    lines = []  # Initialize an empty list to store the lines.
    current_line = []  # Initialize an empty list to store the words of the current line.

    current_length = 0  # Initialize the length of the current line.

    for word in words:  # Loop through each word in the text.
        if current_length + len(word) + len(current_line) <= width:  # Check if adding the word exceeds the width.
            current_line.append(word)  # Add the word to the current line.
            current_length += len(word)  # Update the length of the current line.
        else:  # If adding the word exceeds the width, finalize the current line.
            lines.append(current_line)  # Append the current line to the lines list.
            current_line = [word]  # Start a new line with the current word.
            current_length = len(word)  # Reset the length of the current line.
    
    if current_line:  # Append the last line if it exists.
        lines.append(current_line)

    justified_lines = []  # Initialize an empty list to store the justified lines.

    for line in lines[:-1]:  # Loop through all lines except the last one.
        if len(line) == 1:  # If the line has only one word, left-align it.
            justified_lines.append(line[0].ljust(width))
            continue
        
        total_spaces = width - sum(len(word) for word in line)  # Calculate total spaces to be added.
        spaces_between_words, extra_spaces = divvy_up_spaces(total_spaces, len(line) - 1)  # Distribute spaces.

        justified_line = ""  # Initialize an empty string for the justified line.
        for i in range(len(line) - 1):  # Loop through each word in the line except the last one.
            justified_line += line[i] + " " * (spaces_between_words + (1 if i < extra_spaces else 0))  # Add spaces.
        
        justified_line += line[-1]  # Add the last word to the justified line.
        justified_lines.append(justified_line)  # Append the justified line to the list.
    
    last_line = " ".join(lines[-1])  # Join the last line with spaces.
    justified_lines.append(last_line.ljust(width))  # Left-align the last line.

    return justified_lines  # Return the list of justified lines.
```

### 5. `divvy_up_spaces`

#### Purpose:

To distribute the total spaces evenly between the slots (spaces between words).

```python
def divvy_up_spaces(total_spaces, slots):
    return divmod(total_spaces, slots)  # Return the quotient and remainder when dividing total_spaces by slots.
```
