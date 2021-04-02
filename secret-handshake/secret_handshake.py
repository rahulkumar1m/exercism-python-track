handshake = {
    1 : "wink",
    10 : "double blink",
    100 : "close your eyes",
    1000 : "jump"
}

def commands(number: int):
    # converting the number to binary format
    num_bin = "{0:b}".format(number)
    
    # declaring list to store the secret handshake
    secret = []

    # initializing counter to count the number of places we have iterated in binary
    counter = 0

    # looping over places of binary number and 
    for c in reversed(num_bin):
        if c != '0':
            secret.append(handshake[int(c)*(10**counter)])
        counter += 1
        if counter >= 4:
            break

    # reversing the list if the
    if len(num_bin) >= 5:
        if num_bin[-5] == "1":
            secret = secret[::-1]

    return secret