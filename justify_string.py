def left_align(text, width):
    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        if len(current_line) + len(word) + 1 <= width:
            if current_line:
                current_line += " " + word
            else:
                current_line = word
        else:
            lines.append(current_line)
            current_line = word
    
    if current_line:
        lines.append(current_line)
    
    return lines

def right_align(text, width):
    lines = left_align(text, width)
    for i in range(len(lines)):
        lines[i] = lines[i].rjust(width)
    return lines

def center_align(text, width):
    lines = left_align(text, width)
    for i in range(len(lines)):
        lines[i] = lines[i].center(width)
    return lines

def justify_align(text, width):
    words = text.split()
    lines = []
    current_line = []

    current_length = 0

    for word in words:
        if current_length + len(word) + len(current_line) <= width:
            current_line.append(word)
            current_length += len(word)
        else:
            lines.append(current_line)
            current_line = [word]
            current_length = len(word)
    
    if current_line:
        lines.append(current_line)

    justified_lines = []

    for line in lines[:-1]:
        if len(line) == 1:
            justified_lines.append(line[0].ljust(width))
            continue
        
        total_spaces = width - sum(len(word) for word in line)
        spaces_between_words, extra_spaces = divvy_up_spaces(total_spaces, len(line) - 1)

        justified_line = ""
        for i in range(len(line) - 1):
            justified_line += line[i] + " " * (spaces_between_words + (1 if i < extra_spaces else 0))
        
        justified_line += line[-1]
        justified_lines.append(justified_line)
    
    last_line = " ".join(lines[-1])
    justified_lines.append(last_line.ljust(width))

    return justified_lines

def divvy_up_spaces(total_spaces, slots):
    return divmod(total_spaces, slots)

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
