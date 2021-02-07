def saddle_points(matrix):
    if len(set(map(len, matrix))) > 1:
        raise ValueError("Irregular Matrix")

    matrix_ = list(zip(*matrix))
    points = []

    for i, row in enumerate(matrix):
        for j, x in enumerate(row):
            if x == max(row) and x == min(matrix_[j]):
                points.append({"row" : i+1, "column" : j+1})
    return points
