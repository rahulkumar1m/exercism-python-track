points = {}
for letters, point in {'AEIOULNRST' : 1,
            'DG' : 2,
            'BCMP' : 3,
            'FHVWY' : 4,
            'K' : 5,
            'JX' : 8,
            'QZ' : 10}.items():
    points.update({letter: point for letter in letters})

def score(word: str) -> int:
   return sum([points[letter] for letter in word.upper()])
