class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

person = Person("Alice", 25) # type: ignore[assignment]

print(person.name) # type: ignore[attr-defined]
print(person.age)  # type: ignore[attr-defined]
