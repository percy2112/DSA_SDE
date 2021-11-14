def PascalTriangle(numRows):
    if numRows == 1:
        return [[1]]
    if numRows == 2:
        return [[1], [1, 1]]
    else:
        pascal_list = [[1], [1, 1]]
        for i in range(2, numRows):
            temp_list = [1]
            for j in range(1, i):
                temp_list.append(pascal_list[i - 1][j - 1] + pascal_list[i - 1][j])
            temp_list.append(1)
            pascal_list.append(temp_list)
    return pascal_list


print(PascalTriangle(5))
