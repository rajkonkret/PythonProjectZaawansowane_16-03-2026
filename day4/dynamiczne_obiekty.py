# uproszczony StatePattern

class DynamicBehavior:
    def __init__(self):
        self.state = "initial"

    def change_behavior(self):
        if self.state == "initial":
            self.state = "changed"
            self.execute = self.changed_behavior
        elif self.state == "changed":
            self.state = "final"
            # self.execute = self.changed_behavior
            self.execute = self.final_behavior
        else:
            print("Obiekt zakońćzył działanie")

    def intial_behavior(self):
        return "Zachowanie początkowe"

    def changed_behavior(self):
        return "Zachowanie zmienione"

    def final_behavior(self):
        return "Zachowanie końćowe"

    def execute(self):
        return self.intial_behavior()


obj = DynamicBehavior()
print(obj.execute())
# Zachowanie początkowe

obj.change_behavior()
print(obj.execute())
# Zachowanie zmienione

obj.change_behavior()
print(obj.execute())  # Zachowanie zmienione
# Zachowanie końćowe
