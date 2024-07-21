def left_align(text, width):
    words = text.split()                                      # Split the text into individual words.
    lines = []                                                # Initialize an empty list to store the lines.
    current_line = ""                                         # Initialize an empty string to store the current line.

    for word in words:                                        # Loop through each word in the text.
        if len(current_line) + len(word) + 1 <= width:        # Check if adding the word exceeds the width.
            if current_line:                                  # If current_line is not empty, add a space before the word.
                current_line += " " + word
            else:                                             # If current_line is empty, start it with the word.
                current_line = word
        else:                                                 # If adding the word exceeds the width, finalize the current line.
            lines.append(current_line)                        # Append the current line to the lines list.
            current_line = word                               # Start a new line with the current word.
    
    if current_line:                                          # Append the last line if it exists.
        lines.append(current_line)
    
    return lines                                              # Return the list of left-aligned lines.

def right_align(text, width):
    lines = left_align(text, width)                           # First, get the left-aligned lines.
    right_aligned_lines = []
    for line in lines:                                        # Loop through each line.
        spaces_needed = width - len(line)                     # Calculate the number of spaces needed.
        right_aligned_lines.append(' ' * spaces_needed + line) # Add spaces to the beginning.
    return right_aligned_lines                                # Return the list of right-aligned lines.

def center_align(text, width):
    lines = left_align(text, width)                           # First, get the left-aligned lines.
    center_aligned_lines = []
    for line in lines:                                        # Loop through each line.
        total_padding = width - len(line)                     # Calculate the total padding needed.
        left_padding = total_padding // 2                     # Calculate left padding.
        right_padding = total_padding - left_padding          # Calculate right padding.
        center_aligned_lines.append(' ' * left_padding + line + ' ' * right_padding) # Add padding on both sides.
    return center_aligned_lines                               # Return the list of center-aligned lines.

def justify_align(text, width):
    words = text.split()                                      # Split the text into individual words.
    lines = []                                                # Initialize an empty list to store the lines.
    current_line = []                                         # Initialize an empty list to store the words of the current line.

    current_length = 0                                        # Initialize the length of the current line.

    for word in words:                                        # Loop through each word in the text.
        if current_length + len(word) + len(current_line) <= width:  # Check if adding the word exceeds the width.
            current_line.append(word)                         # Add the word to the current line.
            current_length += len(word)                       # Update the length of the current line.
        else:                                                 # If adding the word exceeds the width, finalize the current line.
            lines.append(current_line)                        # Append the current line to the lines list.
            current_line = [word]                             # Start a new line with the current word.
            current_length = len(word)                        # Reset the length of the current line.
    
    if current_line:                                          # Append the last line if it exists.
        lines.append(current_line)

    justified_lines = []                                       # Initialize an empty list to store the justified lines.

    for line in lines[:-1]:                                    # Loop through all lines except the last one.
        if len(line) == 1:                                     # If the line has only one word, left-align it.
            justified_lines.append(line[0] + ' ' * (width - len(line[0])))
            continue
        
        total_spaces = width - sum(len(word) for word in line)  # Calculate total spaces to be added.
        spaces_between_words, extra_spaces = divvy_up_spaces(total_spaces, len(line) - 1)  # Distribute spaces.

        justified_line = ""                                     # Initialize an empty string for the justified line.
        for i in range(len(line) - 1):                          # Loop through each word in the line except the last one.
            justified_line += line[i] + " " * (spaces_between_words + (1 if i < extra_spaces else 0))  # Add spaces.
        
        justified_line += line[-1]                               # Add the last word to the justified line.
        justified_lines.append(justified_line)                   # Append the justified line to the list.
    
    last_line = " ".join(lines[-1])                              # Join the last line with spaces.
    justified_lines.append(last_line + ' ' * (width - len(last_line)))  # Left-align the last line.

    return justified_lines                                       # Return the list of justified lines.

def divvy_up_spaces(total_spaces, slots):
    return divmod(total_spaces, slots)                           # Return the quotient and remainder when dividing total_spaces by slots.

def print_lines(lines):
    for line in lines:
        print(f"{line}")

text = input("Enter a sentence:")
width = int(input("Enter the width:"))

print("Left Aligned:")
print_lines(left_align(text, width))

print("\nRight Aligned:")
print_lines(right_align(text, width))

print("\nCenter Aligned:")
print_lines(center_align(text, width))

print("\nJustified:")
print_lines(justify_align(text, width))
