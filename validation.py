row1 = [3,5,6,9,4,8,7,1,2]
row2 = [1,2,4,3,6,7,5,9,8]
row3 = [7,8,9,1,2,5,6,3,4]
row4 = [4,1,3,6,8,9,2,7,5]
row5 = [8,7,5,2,1,3,4,6,9]
row6 = [6,9,2,5,7,4,1,8,3]
row7 = [5,3,7,4,9,1,8,2,6]
row8 = [2,4,8,7,3,6,9,5,1]
row9 = [9,6,1,8,5,2,3,4,7]

all_rows = [
    row1,
    row2,
    row3,
    row4,
    row5,
    row6,
    row7,
    row8,
    row9
]

column1 = [
    row1[0],
    row2[0],
    row3[0],
    row4[0],
    row5[0],
    row6[0],
    row7[0],
    row8[0],
    row9[0]
    ]

column2 = [
    row1[1],
    row2[1],
    row3[1],
    row4[1],
    row5[1],
    row6[1],
    row7[1],
    row8[1],
    row9[1]
]

column3 = [
    row1[2],
    row2[2],
    row3[2],
    row4[2],
    row5[2],
    row6[2],
    row7[2],
    row8[2],
    row9[2]
]

column4 = [
    row1[3],
    row2[3],
    row3[3],
    row4[3],
    row5[3],
    row6[3],
    row7[3],
    row8[3],
    row9[3]
]

column5 = [
    row1[4],
    row2[4],
    row3[4],
    row4[4],
    row5[4],
    row6[4],
    row7[4],
    row8[4],
    row9[4]
]

column6 = [
    row1[5],
    row2[5],
    row3[5],
    row4[5],
    row5[5],
    row6[5],
    row7[5],
    row8[5],
    row9[5]
]

column7 = [
    row1[6],
    row2[6],
    row3[6],
    row4[6],
    row5[6],
    row6[6],
    row7[6],
    row8[6],
    row9[6]
]

column8 = [
    row1[7],
    row2[7],
    row3[7],
    row4[7],
    row5[7],
    row6[7],
    row7[7],
    row8[7],
    row9[7]
]

column9 = [
    row1[8],
    row2[8],
    row3[8],
    row4[8],
    row5[8],
    row6[8],
    row7[8],
    row8[8],
    row9[8]
]

all_columns = [
    column1,
    column2,
    column3,
    column4,
    column5,
    column6,
    column7,
    column8,
    column9
]

test_list = (
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9
)

i = 1
Row_Test = 1
for row in all_rows:
    if all(x in row for x in test_list):
        Row_Test = Row_Test + 1
        i += 1
    else:
        print("Row Error: " + str(i))
        i += 1
i = 1
Column_Test = 1
for column in all_columns:
    if all(x in column for x in test_list):
        Column_Test = Column_Test + 1
        i += 1
    else:
        print("Column Error: " + str(i))
        i += 1

square1 = [
    row1[0],
    row1[1],
    row1[2],
    row2[0],
    row2[1],
    row2[2],
    row3[0],
    row3[1],
    row3[2]
]
square2 = [
    row1[3],
    row1[4],
    row1[5],
    row2[3],
    row2[4],
    row2[5],
    row3[3],
    row3[4],
    row3[5]
]
square3 = [
    row1[6],
    row1[7],
    row1[8],
    row2[6],
    row2[7],
    row2[8],
    row3[6],
    row3[7],
    row3[8]
]
square4 = [
    row4[0],
    row4[1],
    row4[2],
    row5[0],
    row5[1],
    row5[2],
    row6[0],
    row6[1],
    row6[2]
]
square5 = [
    row4[3],
    row4[4],
    row4[5],
    row5[3],
    row5[4],
    row5[5],
    row6[3],
    row6[4],
    row6[5]
]
square6 = [
    row4[6],
    row4[7],
    row4[8],
    row5[6],
    row5[7],
    row5[8],
    row6[6],
    row6[7],
    row6[8]
]
square7 = [
    row7[0],
    row7[1],
    row7[2],
    row8[0],
    row8[1],
    row8[2],
    row9[0],
    row9[1],
    row9[2]
]
square8 = [
    row7[3],
    row7[4],
    row7[5],
    row8[3],
    row8[4],
    row8[5],
    row9[3],
    row9[4],
    row9[5]
]
square9 = [
    row7[6],
    row7[7],
    row7[8],
    row8[6],
    row8[7],
    row8[8],
    row9[6],
    row9[7],
    row9[8]
]
all_squares = [
    square1,
    square2,
    square3,
    square4,
    square5,
    square6,
    square7,
    square8,
    square9
]
i = 1
Square_Test = 1
for square in all_squares:
    if all(x in square for x in test_list):
        Square_Test = Square_Test + 1
        i += 1
    else:
        print("Square Error: " + str(i))
        i += 1

if Row_Test == 10 and Column_Test == 10 and Square_Test == 10:
    print("Puzzle is valid")
else:
    print("Try to find the errors...")