from pickletools import read_float8
from typing import Protocol, Union


class Convertible(Protocol):
    def convert(self, data: str) -> Union[int, float]:
        pass


# implementacja protokołu
class IntegerConverter:
    def convert(selfself, data: str) -> int:
        return int(data)


class FloatConverter:
    def convert(self, data: str) -> float:
        return float(data)


class BoolConverter:
    def convert(self, data: str) -> bool:
        data = float(data)
        return bool(data)


def converter_data(converter: Convertible, data: str) -> Union[int, float]:
    return converter.convert(data)


int_conv = IntegerConverter()
float_conv = FloatConverter()
bool_conv = BoolConverter()

res_int = converter_data(int_conv, "7890")
res_float = converter_data(float_conv, "0.789")
res_bool = converter_data(bool_conv, "1")
res_bool2 = converter_data(bool_conv, "0")

print(f"Konwersja int: {res_int} -> typ {type(res_int)}")
print(f"Konwersja float: {res_float} -> typ {type(res_float)}")
print(f"Konwersja bool: {res_bool} -> typ {type(res_bool)}")
print(f"Konwersja bool: {res_bool2} -> typ {type(res_bool2)}")
# Konwersja int: 7890 -> typ <class 'int'>
# Konwersja float: 0.789 -> typ <class 'float'>
# Konwersja bool: True -> typ <class 'bool'>
# Konwersja bool: False -> typ <class 'bool'>
