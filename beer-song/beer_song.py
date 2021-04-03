def recite(start: int, take:int=1) -> list:
    # storing parts of the lyrics which are repetitive
    lyrics = ['bottles of beer', 'on the wall', 'Take one down and pass it around', ]

    #Declaring a list to store the lyrics of the song
    song = []

    while(take):
        # Taking care of case when we have 1 bottle of beer
        if start == 1:
            song.append("{} bottle of beer {}, {} bottle of beer.".format(start, lyrics[1], start))
            song.append("Take it down and pass it around, no more {} {}.".format(lyrics[0], lyrics[1]))
            if take != 1:
                song.append("")
            take -= 1
            start -= 1
        # Taking care of case when we have 0 bottle of beer
        elif start == 0:
            song.append("No more {} {}, no more {}.".format(lyrics[0], lyrics[1], lyrics[0]))
            song.append("Go to the store and buy some more, 99 {} {}.".format(lyrics[0], lyrics[1]))
            # song.append("")
            take -= 1
            start -= 1
        else:
            song.append("{} {} {}, {} {}.".format(start, lyrics[0], lyrics[1], start, lyrics[0]))
            # Taking care of case when we have 2 bottles of beer and 1 is left
            if start == 2:
                song.append("{}, {} bottle of beer {}.".format(lyrics[2], start-1, lyrics[1]))
            else:
                song.append("{}, {} {} {}.".format(lyrics[2], start-1, lyrics[0], lyrics[1]))
            if take != 1:
                song.append("")
            take -= 1
            start -= 1
    
    return song
