import re
def abbreviate(words: str)-> str:
    # make a list of all the words in the string
    word = re.findall(r"[a-zA-Z']+", words)

    # Join & return the uppercase of first letter of each word
    return "".join([x[0].upper() for x in word])