"""By starting at the top of the triangle below and moving to 
adjacent numbers on the row below, the maximum total from top to bottom is 23.
                    3
                   7 4
                  2 4 6
                 8 5 9 3
That is, 3 + 7 + 4 + 9 = 23.
Find the maximum total from top to bottom of the text file in test_files:
"""
# figure out

from pathlib import Path
import math, statistics, numpy as np

problem = Path("text_files/p067_triangle.txt").read_text()
problem = problem.replace("\n", ", ")


teest = "3, 7 4, 2 4 6, 8 5 9 3"
# make the string into a List of Lists
def LOL_builder(string):
  A = string.split(", ")
  B = []
  for string in A:
    List = string.split(" ")
    b = []
    for i in List:
      if i != '':
        b.append(int(i))
    if len(b) > 0:
      B.append(b)
  B_ = B[::-1]
  return B, B_

# build the lists
test, test_ = LOL_builder(teest)
Test, Test_ = test.copy(), test_.copy()

a, b = LOL_builder(problem)
Problem, Problem_ = a.copy(), b.copy() 
Pyramid, Pyramid_ = Problem.copy(), Problem_.copy()

# determines the largest sum of the two numbers below each node
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

#test
def main(Rev_List):
  A = Rev_List.copy()
  for i in range(len(A)-1):
    s = []
    A[i], A[i+1]
    for k in range(len(A[i+1])):
      b = is_below(A[i], A[i+1], A[i+1][k])
      s.append(b)
    A[i+1] = s
    # Test_[i+1] = a
    # print(Test_[i+1])
    # z.append(List[i+1])
  return A[-1][-1]




# for x in Test_:
#   print(x)

print("Main =", main(Test_))
print("Main =", main(Problem_))
print("Main =", main(Pyramid_))


def main2(Regular_List):
    A = Regular_List.copy()
    # for row in the range of [two up from the bottom (100 - 2), 
    # stop at the last one, going downward]
    for y in range(len(A)-2,-1,-1):
        # for x in range from 0 to (len of the list - 1)
        # in order to call it use range
        for x in range(len(A[y])):
            # if the one below is greater than (or equal to) the one to the right
            if (A[y+1][x] >= A[y+1][x+1]):
                # this node = below + this node
                A[y][x] = A[y+1][x] + A[y][x]
            # if the one to the right is greater than below
            if (A[y+1][x+1] > A[y+1][x]):
                # this node = right + this node
                A[y][x] = A[y+1][x+1] + A[y][x]
    return A[0][0]

print("Main 2 =", main2(Test))
print("Main 2 =", main2(Problem))
print("Main 2 =", main2(Pyramid))

          

        
        

