from helpers import analytics
analytics.monitor()

"""The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million."""
# def collatz(x):
#     count = 1
#     temp = x  
#     while temp > 1:
#         if temp % 2 == 0:
#             temp = int(temp/2)
#             if temp in has2:  # calculate temp and check if in cache
#                 count += has2[temp]
#                 break
#             else:
#                 count += 1
#         else:
#             temp = 3*temp + 1
#             if temp in has2:            
#                 count += has2[temp]
#                 break
#             else:
#                 count += 1

#     has2[x] = count
#     return count


print("HI")

def GetLongChain(dict1):
    LongChain = max(dict1, key = lambda k: len(dict1[k]))
    return len(dict1[LongChain]),LongChain

MAX = 1000000
def Main2(limit):
    dict1 = {}
    for i in range(2,limit + 1):
        #variables
        seq = [1]
        seq.append(i)
        while i not in range(1, len(seq) + 1):
            if i % 2 == 0:
                i = i//2
                # if i in dict1:
                #     # print("i in dict1", dict1[i])
                #     seq.append(dict1[i])
                #     break
                seq.append(i)
            else:
                i = 3*i + 1
                # if i in dict1:
                #     seq.append(dict1[i])
                #     break
                seq.append(i)
        dict1[i]=seq
        a, b = GetLongChain(dict1)
    return a, b
    

# print('{0} has {1} elements.'.format(greatest,num))


def main(limit):
    chainLength = [1]
    longest = 0
    gen = 0

    for i in range(2,limit+1):
        chain = 0
        while (i not in range(1,len(chainLength)+1)):
            if i % 2 == 0:
                i = int(i/2)
                chain += 1
            else:
                i = (3*i + 1)
                chain += 1
        chain += chainLength[i-1]
        chainLength.append(chain)

    for i in range(0,len(chainLength)):
        if (chainLength[i] > longest):
            longest = chainLength[i]
            gen = i+1

    return str(gen) + " generates a chain of length " + str(longest)


# print(main(1000000), analytics.lap(), analytics.maxMem())
print(Main2(MAX), analytics.lap(), analytics.maxMem())
            