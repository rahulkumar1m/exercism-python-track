import re
from collections import defaultdict

def count_words(sentence):
    # extract all the words as per definition
    sentence = re.findall(r"\b[\w'-]+\b", sentence.lower().replace('_', ' '))
    counts = defaultdict(lambda: 0)

    # Counting the frequency of each words
    for word in sentence:
        counts[word] += 1
    
    return counts
 