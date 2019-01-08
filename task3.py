import csv
import re

triangle = list()
with open ("zadanie_4_triangle_big.txt", "rt") as f:
    reader = csv.reader(f, delimiter=' ', skipinitialspace=True)
    triangle = list()
    for line in reader:
        line = filter(None,line)
        line = list(map(int, line))
        line.extend([0] * (999 - len(line)))
        triangle.append(line)



for elem in triangle:
    print(elem)
with open('testfile.txt', 'w') as f:
    for item in triangle:
        f.write("%s\n" % item)


len(triangle[0])


def maxPathSum(tri, m, n):
    # loop for bottom-up calculation
    for i in range(m - 1, -1, -1):
        for j in range(i + 1):

            # for each element, check both
            # elements just below the number
            # and below right to the number
            # add the maximum of them to it
            if (tri[i + 1][j] > tri[i + 1][j + 1]):
                tri[i][j] += tri[i + 1][j]
            else:
                tri[i][j] += tri[i + 1][j + 1]

                # return the top element
    # which stores the maximum sum
    return tri[0][0]

print(maxPathSum(triangle,999,999))