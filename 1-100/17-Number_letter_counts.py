"""If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.""
"""

# figure out how many places are in a word

# for a in map(int, pow(2, 1000)):
#     a
# i = 0
# while i < Length:
#     # digits.append(int(char))
#     a = long_num(i)
#     i += 1
#     digits.append(a) Length = int(math.log10(long_num))+1
Max = 1000
#and ****
def wordify(Max):
    dig_dict = {
        0: "",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety"
        }
    Alldigits = ""
    i = 1
    while i < Max+1:
        number = str(i)
        digits = []
        str_digits = ''
        for j in number:
            digits.append(int(j))
        places = len(digits)
        while places > 0:
            if places == 4:
                str_digits += dig_dict[digits[0]]+"thousand"
                places -= 1
                digits.pop(0)
                break
            if places == 3:
                str_digits += dig_dict[digits[0]] +"hundred"
                if i % 100 != 0 and i != 1000:
                    str_digits += "and"
                places -= 1
                digits.pop(0)
            if places == 2:
                tens_place = digits[0]
                ones_place = digits[1]
                number = tens_place*10 + ones_place
                if tens_place > 1:
                    if ones_place > 0:
                        str_digits += dig_dict[tens_place*10] + dig_dict[ones_place]
                    else:
                        str_digits += dig_dict[digits[0]*10]
                        digits.pop(0)
                    places -= 2
                elif tens_place < 1:
                    places -= 1
                    digits.pop(0)
                else:
                    temp = dig_dict[digits[0]*10 + digits[1]] 
                    str_digits += temp
                    places -= 2
                    digits.pop(0)
                    digits.pop(0)
            if places == 1:
                if digits[0] == "0":
                    str_digits += ""
                    places -= 1
                    digits.pop(0)
                else:
                    str_digits += dig_dict[digits[0]]
                    places -= 1
                    digits.pop(0)
        i += 1
        Alldigits += str_digits
    return Alldigits

print(len(wordify(1000)))
            





            
