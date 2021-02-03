def find_anagrams(word, candidates):
    dict_word = {}
    expected_list = []

    for char in word.lower():
        if char in dict_word:
            dict_word[char] += 1
        else:
            dict_word[char] = 1
    
    for candidate in candidates:
        if (len(candidate) != len(word)) | (candidate.lower() == word.lower()):
            continue

        dict_candidate = {}
        for char in candidate.lower():
            if char in dict_candidate:
                dict_candidate[char] += 1
            else:
                dict_candidate[char] = 1
        
        anagram = True
        for key, value in dict_candidate.items():
            if key not in dict_word:
                anagram = False
                break
            elif value != dict_word[key]:
                anagram = False
                break
        
        if anagram:
            expected_list.append(candidate)
    
    return expected_list