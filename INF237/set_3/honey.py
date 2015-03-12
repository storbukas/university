# maximum depth is 14
L = 15

# creates a 3-dimensional array with x,y (width, depth) and z as the steps (1 <= n <= 14)
d = [([([0 for x in xrange(L)]) for y in xrange(L)]) for z in xrange(L)]

# set basecase aka center of array equal to 1
d[7][7][0] = 1

# because we only are supposed to evaluate in a hexagonal matter
# define a way of checking your neighbours:
#
#   check neighbours with x
#
#     0-step      1-step      2-step
#   _ _ _ _ _   _ _ _ _ _   _ _ _ _ _
#   _ x x _ _   _ 1 1 _ _   _ 2 2 _ _
#   _ x 1 x _   _ 1 0 1 _   _ 3 6 3 _
#   _ _ x x _   _ _ 1 1 _   _ _ 2 2 _
#   _ _ _ _ _   _ _ _ _ _   _ _ _ _ _
#

# add to upper step length from current step length value (if within boundaries (0-14)
# outer loop is step-length
for z in range(L-1):
    for x in range(L): # x-coordinates
        for y in range(L): # y-coordinates
            if(x > 0 and y > 0): # x-1, y-1
                d[x][y][z+1]+= d[x-1][y-1][z]
            if(x > 0): # x-1
                d[x][y][z+1] += d[x-1][y][z]
            if(y > 0): # y-1
                d[x][y][z+1] += d[x][y-1][z]
            if(x < 14 and y < 14): # x+1, y+1
                d[x][y][z+1] += d[x+1][y+1][z]
            if(x < 14): # x+1
                d[x][y][z+1] += d[x+1][y][z]
            if(y < 14): # y+1
                d[x][y][z+1] += d[x][y+1][z]

# nr of testcases
testcases = int(raw_input())
for _ in range(testcases):
    n = int(raw_input())
    print(d[7][7][n]) # print out result for step-n
