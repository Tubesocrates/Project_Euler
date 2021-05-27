"""Using names.txt (right click and 'Save Link/Target As...'), 
a 46K text file containing over five-thousand first names, begin by 
sorting it into alphabetical order. Then working out the alphabetical value 
for each name, multiply this value by its alphabetical position in the list to obtain 
a name score.

For example, when the list is sorted into alphabetical order, 
COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""
from pathlib import Path
import math, statistics, numpy as np

A = Path("text_files/p022_names.txt").read_text()#.replace("\n", ",")
A1 = [x.strip('"') for x in A.split(',')]

# print(A1)

letter_score = {"A":1,
                "B":2,
                "C":3,
                "D":4,
                "E":5,
                "F":6,
                "G":7,
                "H":8,
                "I":9,
                "J":10,
                "K":11,
                "L":12,
                "M":13,
                "N":14,
                "O":15,
                "P":16,
                "Q":17,
                "R":18,
                "S":19,
                "T":20,
                "U":21,
                "V":22,
                "W":23,
                "X":24,
                "Y":25,
                "Z":26
                }

def name_score(List_of_names):
    scores = []
    for i, name in enumerate(List_of_names):
        score = 0
        position = i + 1
        # print(name)
        for letter in name:
            # print(letter)
            score += letter_score.get(letter)
        score_pos = score*position
        scores.append(score_pos)
        i += 1
    return sum(scores)
    
A2 = sorted(A1)
# print(A2)

print(name_score(A2))
    


