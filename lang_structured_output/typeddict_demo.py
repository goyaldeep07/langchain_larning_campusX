from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int
    email: str


person = Person(name="John Doe", age=30, email="john.doe@gmail.com")
print(person)