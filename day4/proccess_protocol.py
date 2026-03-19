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
