def annotate(minefield):
    # Function body starts here
    result = []

    if not minefield:
        return []
    else:
        rows = len(minefield)
        columns = len(minefield[0])

        result = [[0 for j in range(columns)] for i in range(rows)]

        for i in range(rows):
            if len(minefield[i]) != columns:
                raise ValueError("NOT uniform rows")
            for j in range(columns):
                if minefield[i][j] not in ['*', ' ']:
                    raise ValueError("Invalid Character")
                elif minefield[i][j] == '*':
                    for k in range(i-1, i+2):
                        for l in range(j-1, j+2):
                            if (k < 0) or (l < 0)  or (k > rows - 1) or (l > columns - 1) or (result[k][l] == '*'):
                                continue
                            elif (k == i and l == j):
                                result[k][l] = '*'
                            else:
                                result[k][l] += 1
        result = [(''.join(map(str, lis))).replace('0', ' ') for lis in result]
        return result
    return []



# print(len("  *  "))