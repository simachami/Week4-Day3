# DESCRIPTION:
# You are stacking some boxes containing gold weights on top of each other. If a box contains more weight than the box below it, it will crash downwards and combine their weights. e.g. If we stack [2] on top of [1], it will crash downwards and become a single box of weight [3].

# [2]
# [1] --> [3]
# Given an array of arrays, return the bottom row (i.e. the last array) after all crashings are complete.

# crashing_weights([[1, 2, 3],  --> [[1, 2,  ],      [[1,  ,  ],
#                   [2, 3, 1],  -->  [2, 3, 4],  -->  [2, 2,  ],
#                   [3, 1, 2]])      [3, 1, 2]]  -->  [3, 4, 6]]

# therefore return [3, 4, 6]
# More details
# boxes can be stacked to any height, and the crashing effect can snowball:

# [3]
# [2]     [5]
# [4] --> [4] --> [9]
# Crashing should always start from as high up as possible -- this can alter the outcome! e.g.

# [3]                      [3]
# [2]     [5]              [2]     [3]
# [1] --> [1] --> [6], not [1] --> [3] 
# Weights will always be integers. The matrix (array of arrays) may have any height or width >= 1, and may not be square, but it will always be "nice" (all rows will have the same number of columns, etc).

def stacked_boxes(alist):
    if len(alist) == 1:
        return alist[0]
    for lst in range(1, len(alist)):
        for i in range(0,len(alist[lst])):
            if alist[lst][i] < alist[lst - 1][i]:
                alist[lst][i] += alist[lst - 1][i]
    return alist[len(alist) - 1]
#O(n*m)
print(stacked_boxes([[1,2,3],[2,3,1],[3,1,2]]))


