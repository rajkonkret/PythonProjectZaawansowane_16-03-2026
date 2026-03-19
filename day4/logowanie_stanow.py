"""
dekorator do logowaia stanu obiektów
Można sledzic zmiany stanó obiektów i kontrolowac jakie metody na nie wpływaja
__setattr__
"""


def log_state_changes(cls):
    class Wrappped(cls):
        def __setattr__(self, key, value):
            if key in self.__dict__:
                old_value = self.__dict__[key]
                print(f"Zmieniono {key} z {old_value} to {value}")
            super().__setattr__(key, value)

    return Wrappped


@log_state_changes
class Document:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def update_content(self, new_content):
        self.content = new_content


doc = Document("Python Tips", "Content about Python!")
doc.update_content("new big content about Python libraries")
print(doc.content)
# Zmieniono content z Content about Python! to new big content about Python libraries
# new big content about Python libraries
