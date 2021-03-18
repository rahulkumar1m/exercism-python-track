def is_paired(input_string: str):
    # Declaring a stack to store the brackets
    bracket_stack = []
    
    # initializing a dictionary to check which bracket correspond to which bracket
    bracket_dict = {
        '[' : ']',
        '{' : '}',
        '(' : ')'
    }

    # Looping through characters to check for brackets
    for _ in input_string:
        if _ in "[{(":
            bracket_stack.append(_)
        elif _ in "]})":
            if (not bracket_stack) or (bracket_dict[bracket_stack.pop()] != _):
                return False

    # if there is still some brackets left in our stack, return False, else True
    if bracket_stack:
        return False
    else:
        return True
