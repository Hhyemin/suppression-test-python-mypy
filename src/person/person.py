class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

person = Person("Alice", 25)  

print(person.name) 
print(person.age)   
