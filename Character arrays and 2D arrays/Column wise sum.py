from sys import stdin
import numpy as np

s = [int(ele) for ele in stdin.readline().strip().split(" ")]

rows = s[0]
cols = s[1]

mat=[]

# Take input from user the elements of an array
slice_from = 2
for row in range(rows):
    row_elmnts = s[slice_from:slice_from+cols]
    mat.append(row_elmnts)
    slice_from = slice_from + cols

sum = np.zeros(cols).astype('int32')
print(sum)
for col in range(cols):
    temp_sum = 0
    for row in range(rows):
        temp_sum = temp_sum + mat[row][col]
    sum[col] = temp_sum

print(sum)

# Take input from user the elements of an array
# for row in range(rows):
#     elmnts = stdin.readline().strip().split(" ")
#     for col in range(cols):
#         arr_2d[row][col] = int(elmnts[col])



