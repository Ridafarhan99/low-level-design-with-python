class Student:
    #Attributes
    name = ""
    age = 1
    gender = ""

# methods
# inside class we have to pass self for any function - object name will be the self
    # constructor / Initializer
    def __init__(self, name, age, gender) -> None:
        self.name = name
        self.age = age
        self.gender = gender

    def set_value(self, name:str, age:int ,gender:str) -> None:
        self.name = name
        self.age = age
        self.gender = gender

    # -> None means it is not returning anything
    def display(self) -> None:
        print(f"Self - > {self}")
        print(f"My name is {self.name}, age is {self.age}")

    def get_age(self) -> int:
        return self.age;


s1 = Student("Tyson", 45, "Male")
s1.set_value("Rida", 23, "Male")
print(s1.name);
print(s1)
s1.display()


s2 = Student("Mike", 43, "Male")
s2.display()
s2.get_age()