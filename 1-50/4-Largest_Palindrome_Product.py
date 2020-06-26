# A palindromic number reads the same both ways. The largest palindrome made from the product of two 
# 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindromic_num(number):
    reverse = int(str(number)[::-1])
    if reverse == number:
        return True
    else: False

# is_palindromic_num(5005)
# is_palindromic_num(5004)
set_list = []
# num2_num1 = []
prod = []
palind = []
def find_palindromic_nums():
    # set original numbers
    #check 900s bc of hunch
    num_1 = 100
    num_2 = 100
    while num_1 < 1000:
        if is_palindromic_num(num_1*num_2):
            if num_1*num_2 not in prod:
                palind.append(num_1*num_2)
        set_list.append({num_1, num_2})
        prod.append(num_1*num_2)
        num_1 += 1
        while num_2 < 1000:
            if {num_2, num_1} not in set_list:
                if is_palindromic_num(num_1*num_2):
                    if num_1*num_2 not in prod:
                        palind.append(num_1*num_2)
                        prod.append(num_1*num_2)
                set_list.append({num_1, num_2})
            num_2 += 1
    return palind

print(find_palindromic_nums())

# set examples
# set_list = [{"a","b"}, {1,4}, {"f",5}]

# if {"b","a"} in set_list:
#     print("good")


# if {5,"f"} in set_list:
#     print("good")

# set_list.append({"g", 23})
# print(set_list)

# if {23,"g"} in set_list:
#     print("good")

