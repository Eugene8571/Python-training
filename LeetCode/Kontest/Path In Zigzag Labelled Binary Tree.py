def bin_tree_path(label):
    row = 0
    n = 1
    while n <= label:
        n += 2 ** row
        row += 1

    A = [label]
    step = label

    R_row = [int(i) for i in range(int(2 ** row / 2), 2 ** row)]
    if row % 2 == 0:
        R_row = R_row[::-1]
    position = R_row.index(step)
    row -= 1

    while row >= 1:
        R_row = [int(i) for i in range(int(2 ** row / 2), 2 ** row)]
        if row % 2 == 0:
            R_row = R_row[::-1]
        position = position // 2
        A.append(R_row[position])

        step = step // 2

        row -= 1

    return A[::-1]


print(bin_tree_path(12))
