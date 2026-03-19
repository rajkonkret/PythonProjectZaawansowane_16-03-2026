from typing import Protocol, List, Any
import numpy as np


class DataProcessor(Protocol):
    def process(self, data: List[Any]) -> List[Any]:
        pass


class NumerProcessor:
    def process(self, data: List[Any]) -> List[Any]:
        return [item * 2 for item in data if isinstance(item, int) or isinstance(item, float)]


class StringProcessor:
    def process(self, data: List[Any]) -> List[Any]:
        return [item.upper() for item in data if isinstance(item, str)]


# przyjmuje obiekt zgodny z protokołem DataProcessor
def process_data(processor: DataProcessor, data: List[Any]) -> List[Any]:
    return processor.process(data)


number_processor = NumerProcessor()
string_proessor = StringProcessor()

data_to_process = [1, 2, "ok", 3, 4, 5, 6, 6.78, 0, 53, "hej", "zielony", 78.5, "456", "r", [3, 6, "inny"]]
array_tonp = [4, 7, 4, 6, 3, 78, 3, "tak", 63, 678, 33, 5, 4.44, "nie"]
array_mix = np.array(array_tonp)
print(array_tonp)
print(type(array_tonp))  # <class 'list'>

proc_nb = process_data(number_processor, data_to_process)
print(f"Wynik dla liczb: {proc_nb}")
# Wynik dla liczb: [2, 4, 6, 8, 10, 12, 13.56, 0, 106, 157.0]

proc_str = process_data(string_proessor, data_to_process)
print(f"Wynik dla tekstu: {proc_str}")
# Wynik dla tekstu: ['OK', 'HEJ', 'ZIELONY', '456', 'R']

print(f"Test dla NumPy")

proc_nb_np = process_data(number_processor, array_tonp)
proc_str_np = process_data(string_proessor, array_tonp)
print(f"Wynik dla liczb: {proc_nb_np}")
print(f"Wynik dla tekstu: {proc_str_np}")
# Wynik dla liczb: [8, 14, 8, 12, 6, 156, 6, 126, 1356, 66, 10, 8.88]
# Wynik dla tekstu: ['TAK', 'NIE']