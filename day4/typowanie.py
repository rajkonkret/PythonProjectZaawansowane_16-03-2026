# użycie typing
from typing import TypedDict, get_origin


class User(TypedDict):
    name: str
    age: int
    email: str


def print_user_info(user: User) -> None:
    print(f"Name: {user['name']}, Age: {user['age']}, e-mail: {user['email']}")


user_data = {'name': "Leon", 'age': 40, 'email': 'leon@abc.pl'}
print_user_info(user_data)  # Name: Leon, Age: 40, e-mail: leon@abc.pl

# złożone aliasy typów
from typing import List, Tuple, Union

Coordinate = Tuple[float, float]
Path = List[Coordinate]
CoordinateError = Union[Coordinate, int]


def validate_coordinaate(coord: CoordinateError) -> bool:
    if isinstance(coord, str):
        print(f"Error: {coord}")
        return False
    return True


example_path = [(0.0, 1.0), (2.5, 3.5), (4.0, -1.2), ("True", True)]

