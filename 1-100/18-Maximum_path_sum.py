"""By starting at the top of the triangle below and moving to 
adjacent numbers on the row below, the maximum total from top to bottom is 23.
                    3
                   7 4
                  2 4 6
                 8 5 9 3
That is, 3 + 7 + 4 + 9 = 23.
Find the maximum total from top to bottom of the triangle below:
                75
               95 64
             17 47 82
            18 35 87 10
           20 04 82 47 65
          19 01 23 75 03 34
         88 02 77 73 07 63 67
        99 65 04 28 06 16 70 92
      41 41 26 56 83 40 80 70 33
     41 48 72 33 47 32 37 16 94 29
    53 71 44 65 25 43 91 52 97 51 14
   70 11 33 28 77 73 17 78 39 68 17 57
  91 71 52 38 17 14 91 43 58 50 27 29 48
 63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
note: As there are only 16384 routes, it is possible to solve this problem 
by trying every route. However, Problem 67, is the same challenge with a 
triangle containing one-hundred rows; it cannot be solved by brute force, 
and requires a clever method! ;o)
"""

import math, statistics, numpy as np

problem = "75, 95 64, 17 47 82, 18 35 87 10, 20 04 82 47 65, 19 01 23 75 03 34, 88 02 77 73 07 63 67, 99 65 04 28 06 16 70 92, 41 41 26 56 83 40 80 70 33, 41 48 72 33 47 32 37 16 94 29, 53 71 44 65 25 43 91 52 97 51 14, 70 11 33 28 77 73 17 78 39 68 17 57, 91 71 52 38 17 14 91 43 58 50 27 29 48, 63 66 04 68 89 53 67 30 73 16 69 87 40 31, 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"
test = "3, 7 4, 2 4 6, 8 5 9 3"
# make the string into a List of Lists
def LOL_builder(string):
  A = string.split(", ")
  B = []
  for string in A:
    List = string.split(" ")
    b = []
    for i in List:
      b.append(int(i))
    B.append(b)
  B_ = B[::-1]
  return B, B_
# build the lists
Test, Test_ = LOL_builder(test)
Problem, Problem_ = LOL_builder(problem)

# useful definitions
def list_swapper(list1, list2):
  temp = list2
  list2 = list1
  list1 = temp
  return list1, list2

# print(list_swapper(Problem[0], Problem[1]))

# determines the numbers that are sufficiently large
# didnt use
def is_below(list1, list2, element_L2):
  L1, L2 = len(list1), len(list2)
  # we are picking L1 being the "bottom row" and L2 being the one above it
  index2 = list2.index(element_L2)
  # middle case i.e. maps to two options, the node right below and to the right
  index_1 = index2
  index_2 = index2 + 1
  sum_1 = list2[index2] + list1[index_1]
  sum_2 = list2[index2] + list1[index_2]

  return max(sum_1, sum_2)

for x in Test_:
  print(x)

#test
def Test_prog1(Test_):
  i = 0
  z = []
  while i < len(Test_) - 1:
    a = []
    Test_[i], Test_[i+1]
    for k in Test_[i+1]:
      b = is_below(Test_[i], Test_[i+1], k)
      a.append(b)
    Test_[i+1] = a
    # print(Test_[i+1])
    z.append(Test_[i+1])
    i += 1

  return f"{z[-1]}"

print(Test_prog1(Test_))
print(Test_prog1(Problem_))



def pathfinder(list1, list2):
    L1, L2 = len(list1), len(list2)
    if L2 > L1:# ensure len(l1) is > len(l2)
        list1, list2 = list_swapper(L1, L2)
        L1, L2 = len(list1), len(list2)
    paths = []
    if len(list1) + len(list2) >= 3:
      l1 = energy_pack(list1)
      l2 = energy_pack(list2)
      print(l1)
      ListA = []
      
      for element in l1:
          temp = []
          a, b, c = is_next(list1, list2, element)
          print(a, b)
          if a in l1:
            if b or c in l2:
              temp.append(a)
              if c not in l2:
                temp.append(b)
              if b not in l2:
                temp.append(c)
            ListA.append(temp)
            if c in l2:
              temp.append(a)
              temp.append(c)
              break
          ListA.append(temp)


    return f"Path1_2 = {ListA}"

def energy_pack(List):
    biggest_nums = []
    row = List
    row_num = len(row)
    st_dev = statistics.pstdev(row)
    avg = sum(row)/len(row)
    Max = max(row)
    for element in row:
        if element > Max - 1.75*st_dev:
            biggest_nums.append(element)
    return biggest_nums

# given two lists, finds the largest list, 
# find the biggest sum that is adjacent,
# remember the path(s)
# didnt use
def is_next(list1, list2, element_L1):
    L1, L2 = len(list1), len(list2)
    index1 = list1.index(element_L1)
    # print(f"index1: {index1}, {L1}, {L2}")
    values = []
    # middle case i.e. maps to two options, below and to the right
    if index1 < L2:
      index_1 = index1
      if index1 > 0:
        index_2 = index1 - 1
        tup_2 = list1[index1], list2[index_2]
        values.append(tup_2)
        tup_1 = list1[index1], list2[index_1]
        values.append(tup_1)
      if index1 == 0:
        tup_1 = list1[index1], list2[index_1]
        values.append(tup_1)
      
    # left case, maps to one below
    elif index1 == 0:
      index_1 = index1
      tup_1 = [list1[index1], list2[index_1]]
      values.append(tup_1)
    # right case, maps to the left
    elif index1 >= L2 - 1:
      index_1 = index1 - 1
      index_2 = index1
      tup_1 = list1[index1], list2[index_1]
      values.append(tup_1)
      if list2[index_1] != list2[-1]:
        tup_2 = list1[index1], list2[-1]
        values.append(tup_2)
      

    # print(f"Index1 = {index1}, {list1[index1]}, Index2 = {index2}, {list2[index2]}")
    return values[:]

# bad
def brute_force_reverse(List_of_Lists):
    rev_lists = List_of_Lists[::-1]
    len_LOL = len(List_of_Lists)
    count = 1
    list_of_bigs = []
    for row in rev_lists:
        biggest_nums = []
        row_num = len(row)
        st_dev = statistics.pstdev(row)
        avg = sum(row)/len(row)
        Max = max(row)
        for element in row:
          if element > Max - 1.5*st_dev:
            biggest_nums.append(element)
        list_of_bigs.append(biggest_nums)
    

          

          

          

        
        
        

