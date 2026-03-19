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
print(validate_coordinaate(example_path[-1]))  # True
print(validate_coordinaate("Invalidate coordinate"))
# Error: Invalidate coordinate
# False


g = get_origin(Coordinate)
print(g)  # <class 'tuple'>


# poszczególne elemnty
def validate_coordinaate(coord: Coordinate) -> bool:
    if isinstance(coord, get_origin(Coordinate)):
        print(f"Error: {coord}")
        return False
    return True


example_path = [(0.0, 1.0), (2.5, 3.5), (4.0, -1.2), ("True", True)]
print(validate_coordinaate(example_path[-1]))  # ostatni element -> ("True", True)
# Error: ('True', True)
# False

# Protocol
from typing import Protocol


class Runner(Protocol):
    def run(self) -> str:
        ...

    def finish_time(self) -> float:
        ...


class Athlete:
    def run(self) -> str:
        return "Athlete is running"

    def finish_time(self):
        return 1.15


class Robot:
    def run(self) -> str:
        return "robot is running"

    def finish_time(self) -> float:
        return 1.12


def start_race(participiant: Runner) -> None:
    print(participiant.run())
    print(participiant.finish_time())
