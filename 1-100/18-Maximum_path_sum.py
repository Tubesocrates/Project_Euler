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

    

          

          

          

        
        
        

