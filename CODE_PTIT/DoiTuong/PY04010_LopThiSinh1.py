class Student:
    def __init__(self, name, birth, s1, s2, s3):
        self.name = name 
        self.birth = birth
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
    
    def totalScore(self):
        return self.s1 + self.s2 + self.s3
    
    def __str__(self):
        return f"{self.name} {self.birth} {self.totalScore():.1f}"

#main
student = Student(input(), input(), float(input()), float(input()), float(input()))
print(student)