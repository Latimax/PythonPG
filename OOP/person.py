class Person:
    def __init__(self, name, age, country, gender ):
        self.name = name
        self.age = age
        self.country = country
        self.gender = gender

p1 = Person("Abdullateef", 27, "Nigeria", "Male")
print(f"Your name is {p1.name}\n Age is {p1.age}\n Country is {p1.country}\n Gender is {p1.gender}")