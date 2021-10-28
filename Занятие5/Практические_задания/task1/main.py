# if __name__ == "__main__":
#     #matrix = [
#         [1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9]
#     ]

    #for row in range(len(matrix)):
        #for col in range(len(matrix[0])):
            #print(matrix[row][col], end=" ")
        #print()

count_row = 10
count_col = 10
matrix_ = [
    [i * j for j in range(1, count_col)]
    for i in range(1, count_row)
]

for row in range(len(matrix_)):
    for col in range(len(matrix_[0])):
        print(f'{matrix_[row][col]:2}', end=" ")
    print()