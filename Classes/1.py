class student:
    student_count = 0
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        student.student_count += 1
        
    def mean_grade(self):
        return sum(self.grade) / len(self.grade)
    def correct_name(self):
        return self.name.upper()
    def adult(self):
        return self.age >= 18
s1 = student("Alice", 20, [85, 90, 78])
s2 = student("Bob", 17, [80, 75, 88])
print(student.student_count)