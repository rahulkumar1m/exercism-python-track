class Garden:
    def __init__(self, diagram: str, students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']):
        self.diagram = diagram.splitlines()
        self.students = sorted(students)
        self.plant = {'V': 'Violets',
                    'R': 'Radishes',
                    'C': 'Clover',
                    'G': 'Grass'
        }

    def plants(self, student: str) -> list:
        # Finding the index of the sought student
        idx = (self.students.index(student) + 1) * 2

        # Declaring a list to store the result
        result = []

        # Iterating over the two lines of sills on windows to get the plants planted by sought student
        for line in self.diagram:
            result.append(self.plant[line[idx - 2]])
            result.append(self.plant[line[idx - 1]])

        return result