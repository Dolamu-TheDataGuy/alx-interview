#!/usr/bin/python3

def pascal_triangle(n):
    """
    implementation of pascal's triangle

    """
    pascal_list = [[1], [1,1]]
    if n <= 0:
        return []

    if n == 1:
        return [pascal_list[0]]
    
    if n == 2:
        return pascal_list

    for i in range(3, n+1):
        prev_row = pascal_list[-1]
        prev_len = len(prev_row)
        temp = list(range(prev_len+1))
        for  a in range(prev_len):
            if a == 0:
                temp[a] = prev_row[a]
            else:
                temp[a] = prev_row[a] + prev_row[a-1]
        temp[-1] = 1
        prev_row = temp
        pascal_list.append(temp)
    return pascal_list
