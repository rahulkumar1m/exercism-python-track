import re

def count_words(sentence):
    # extract all the words as per definition
    sentence = re.findall(r"\b[\w'-]+\b", sentence.lower().replace('_', ' '))
    counts = {}

    # Counting the frequency of each words
    for word in sentence:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    
    return counts
