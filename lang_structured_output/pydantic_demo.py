from pydantic import BaseModel, Field


class Student(BaseModel):
    name: str = Field(..., description="The name of the student", default="John Doe")


# student = Student(name="John Doe")
student = Student()
print(student)
