from pydantic import Field
from pydantic.dataclasses import dataclass
import dataclasses
from typing import List, Optional


@dataclass
class User:
    id: int
    height: Optional[int] = Field(None, title="wzrost w cm", ge=50, le=260)
    age: Optional[int] = dataclasses.field(default=None, metadata=dict(title='Wiek użytkownika',
                                                                       description='Nie kłam!'))
    friends: List[int] = dataclasses.field(default_factory=lambda: [0])
    name: str = "Jan Kowlaski"


user = User(id='33')
print(user)
# User(id=33, height=None, age=None, friends=[0], name='Jan Kowlaski')

# us1 = User(64, "Olga Kot", [7, ], 38, 170)
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\AI\PythonProjectZaawansowane_16-03-2026\day3\project_pydantic.py", line 21, in <module>
#     us1 = User(64, "Olga Kot", [7, ], 38, 170)
#   File "C:\Users\CSComarch\AI\PythonProjectZaawansowane_16-03-2026\.venv\Lib\site-packages\pydantic\_internal\_dataclasses.py", line 121, in __init__
#     s.__pydantic_validator__.validate_python(ArgsKwargs(args, kwargs), self_instance=s)
#     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# pydantic_core._pydantic_core.ValidationError: 4 validation errors for User
# 1
#   Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='Olga Kot', input_type=str]
#     For further information visit https://errors.pydantic.dev/2.12/v/int_parsing
# 2
#   Input should be a valid integer [type=int_type, input_value=[7], input_type=list]
#     For further information visit https://errors.pydantic.dev/2.12/v/int_type
# 3
#   Input should be a valid list [type=list_type, input_value=38, input_type=int]
#     For further information visit https://errors.pydantic.dev/2.12/v/list_type
# 4
#   Input should be a valid string [type=string_type, input_value=170, input_type=int]
#     For further information visit https://errors.pydantic.dev/2.12/v/string_type


# us2 = User(75, "Piotr Kamyk", [34, 63, 3], 17, 209)
# print(us2)
# 4
#   Input should be a valid string [type=string_type, input_value=209, input_type=int]
#     For further information visit https://errors.pydantic.dev/2.12/v/string_type
