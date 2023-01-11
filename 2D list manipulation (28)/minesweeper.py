"""this program takes in a grid of hashes and dashes, representing mines and
free spots, and it outputs a grid where each free spot is replaced by a number indicating whether
there is a mine next to it"""

example = [["-", "-", "-", "#", "#",],
           ["-", "#", "-", "-", "",],
           ["-", "-", "#", "-", "-",],
           ["-", "#", "#", "-", "-",],
           ["-", "-", "-", "-", "-",]]


#find the length of the example matrix rows and columns
no_col = len(example[1])
#print(no_col) - for testing

no_rows = len(example)
#print(no_rows) - for testing

#create matrix of zeros to undergo manipulation
zeros = [[0]*(no_col+2) for item in range(no_rows+2)]
nested_list_of_mines = []

#find where mines are
for row_index in range(len(example)):
    for col_index in range(len(example[row_index])):

        # if has in row, grab row index and col index
        if "#" in example[row_index][col_index]:
            mines = [row_index+1, col_index+1]
            nested_list_of_mines.append(mines)

#print example for testinf
for row in example:
    print(row)

# #print mine coords for trsting
# print(nested_list_of_mines)

for coords in nested_list_of_mines:
    #left
    zeros[coords[0]][(coords[1]-1)] += 1
    #right
    zeros[coords[0]][(coords[1] + 1)] += 1
    #up
    zeros[(coords[0] - 1)][coords[1]] += 1
    #down
    zeros[(coords[0] + 1)][coords[1]] += 1
    #up right
    zeros[(coords[0] - 1)][(coords[1] + 1)] += 1
    #up left
    zeros[(coords[0] - 1)][(coords[1] - 1)] += 1
    # down right
    zeros[(coords[0] + 1)][(coords[1] + 1)] += 1
    # down left
    zeros[(coords[0] + 1)][(coords[1] - 1)] += 1

#replace mines
for coords in nested_list_of_mines:
    zeros[coords[0]][coords[1]] = "#"

# #print output for testing
# for row in zeros:
#     print(row)

#strip down to size
new_list = []
for i in range(1, len(zeros)-1):
    new_list_row = zeros[i]
    new_list_cols = new_list_row[1:len(zeros[1])-1]
    new_list.append(new_list_cols)

print()
for row in new_list:
    print(row)

