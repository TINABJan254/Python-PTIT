class Person:
    nationality = "Viet Nam"
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def getAge(self):
        return self.__age
    
p1 = Person("Thien", 23)
p2 = Person("Tran", 32)

print(p1.getAge())