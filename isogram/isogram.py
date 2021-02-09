def is_isogram(string) -> bool:
    # Tokenizing the characters in the string
    string = [char for char in string.lower()]

    # initializing an empty list of characters present in the string
    characters = []

    # if a character from string is already present in our list of characters, we return False
    for char in string:
        if (char == " ") or (char == "-"):
            continue
        elif char in characters:
            return False
        else:
            characters.append(char)
    
    return True
