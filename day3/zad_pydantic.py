from pydantic import BaseModel, ValidationError


# uv add pydantic

class User(BaseModel, validate_assignment=True):
    name: str
    age: int


u = User(name="Jan", age=30)
print(u)  # name='Jan' age=30

# try:
#     u.age = "abc"
# except ValidationError as e:
#     print(e)
# 1 validation error for User
# age
#   Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='abc', input_type=str]
#     For further information visit https://errors.pydantic.dev/2.12/v/int_parsing
#
# Process fin

u.age = "123"
print(type(u.age))  # <class 'int'>

from pydantic import TypeAdapter

adapter = TypeAdapter(list[int])

result = adapter.validate_python([1, 2, "3"])
print(result)  # [1, 2, 3]
