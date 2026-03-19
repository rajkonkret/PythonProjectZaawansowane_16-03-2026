from typing import Protocol


class Executable(Protocol):
    def execute(self) -> str:
        ...


# zwykłą funkcja która nie jest klasą
def mfunkcja() -> str:
    return "funkcja wykonana"


# adaptacja funkcji do protokołu
class FunctionAdapter:
    def __init__(self, func):
        self.func = func

    def execute(self) -> str:
        return self.func()


def run_task(executable: Executable):
    print(executable.execute())  # zakłądamy polimorfizm wg protokołu Executable


adapted_function = FunctionAdapter(mfunkcja)

run_task(adapted_function)  # funkcja wykonana
