def recite(start_verse : int, end_verse : int):
    days = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']
    gifts = ['twelve Drummers Drumming, ', 'eleven Pipers Piping, ', 
            'ten Lords-a-Leaping, ', 'nine Ladies Dancing, ', 
            'eight Maids-a-Milking, ', 'seven Swans-a-Swimming, ', 
            'six Geese-a-Laying, ', 'five Gold Rings, ', 
            'four Calling Birds, ', 'three French Hens, ', 
            'two Turtle Doves, and ', 'a Partridge in a Pear Tree.']
    
    # Initalizing the list to store the lyrics
    recite = []

    for i in range(start_verse - 1, end_verse):
        verse = "On the {} day of Christmas my true love gave to me: ".format(days[i]) + "".join(gifts[11-i:])
        recite.append(verse)

    return recite
