class Matrix:
    def __init__(self, matrix_string: str):
        self.matrix = []
        rows = matrix_string.split('\n')
        
        for row in rows:
            row = row.split(' ')
            row = list(map(int, row))
            self.matrix.append(row)
        print(self.matrix)


    def row(self, index: int) -> list:
        return self.matrix[index-1]


    def column(self, index: int) -> list:
        column = []
        for row in self.matrix:
            column.append(row[index-1])
        return column
