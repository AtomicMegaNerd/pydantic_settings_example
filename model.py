from enum import Enum
from pydantic_settings import BaseSettings


class Status(str, Enum):
    NEW = "New"
    FAILED = "Failed"
    SUCCESSFUL = "Successful"


class Mode(str, Enum):
    EMPLOYEE = "employee"
    STUDENT = "student"
    ROBOT = "robot"


class Common(BaseSettings):
    """
    Common class for Employee, Student and Robot
    """

    name: str
    age: int

    # We can set a default value for status, so we don't need to set it
    # using the environment variable
    status: Status = Status.NEW


class Employee(Common):
    """
    Employee class. The following properties will be loaded from
    the environment variables:
    - name from $NAME
    - age from $AGE
    - salary from $SALARY
    - company from $COMPANY
    """

    salary: float
    company: str

    def __str__(self):
        return (
            f"{self.name} is {self.age} years old and works at "
            f"{self.company} with a salary of {self.salary}"
        )


class Student(Common):
    """
    Student class. The following properties will be loaded from
    the environment variables:
    - name from $NAME
    - age from $AGE
    - grade from $GRADE
    - school from $SCHOOL
    """

    grade: float
    school: str

    def __str__(self):
        return (
            f"{self.name} is {self.age} years old and studies "
            f"at {self.school} with a grade of {self.grade}"
        )


class Robot(Common):
    """
    Robot class. The following properties will be loaded from
    the environment variables:
    - name from $NAME
    - age from $AGE
    - model from $MODEL
    """

    model: str

    def __str__(self):
        return f"{self.name} is {self.age} years old and is a {self.model} robot"
