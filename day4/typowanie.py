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


athlete = Athlete()
robot = Robot()
start_race(athlete)
start_race(robot)
# Athlete is running
# 1.15
# robot is running
# 1.12

# generic
from typing import TypeVar, Generic, List

T = TypeVar("T")


class Stack(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()


stack = Stack[int]()
stack.push(10)
stack.push(12)
stack.push(8.8)
stack.push("abcz")
print(stack.pop())  # abcz


# nowsze podejście, od python 3.12
class Stack[V]:
    def __init__(self) -> None:
        self._container: list[V] = []

    def push(self, item: V) -> None:
        self._container.append(item)

    def pop(self) -> V:
        return self._container.pop()
