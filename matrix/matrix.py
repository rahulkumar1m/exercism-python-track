class Matrix:
    def __init__(self, matrix_string: str):
        rows = matrix_string.splitlines()
        self.matrix = [list(map(int, row.split())) for row in rows]

        # for row in rows:
        #     row = row.split(' ')
        #     row = list(map(int, row))
        #     self.matrix.append(row)
        # print(self.matrix)


    def row(self, index: int) -> list:
        return self.matrix[index-1]


    def column(self, index: int) -> list:
        column = [row[index-1] for row in self.matrix]
        # for row in self.matrix:
        #     column.append(row[index-1])
        return column

