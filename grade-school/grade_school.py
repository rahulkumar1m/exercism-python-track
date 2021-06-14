class School:
    def __init__(self):
        self.students = {}

    def add_student(self, name, grade):
        if grade not in self.students:
            self.students[grade] = []
        self.students[grade].append(name)
        return self.students[grade].sort()

    def roster(self):
        students_roster = []
        grades = list(self.students.keys())
        grades.sort()
        for i in grades:
            for j in self.students[i]:
                students_roster.append(j)
            
        return students_roster

    def grade(self, grade_number):
        if grade_number in self.students:
            return self.students[grade_number]
        return []
