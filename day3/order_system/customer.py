from dataclasses import dataclass


@dataclass
class Customer:
    first_name: str
    last_name: str
    email: str

    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"
