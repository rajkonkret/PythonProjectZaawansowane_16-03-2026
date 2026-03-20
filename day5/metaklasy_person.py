from dataclasses import dataclass, Field
from datetime import datetime

# Field: deafault, default_factory, init, repr, hash, compare,metadata, kw_only, doc

params = {
    "firstname": Field(None, None, True, True, True, True, None, None, None),
    "lastname": Field(None, None, True, True, True, True, None, None, None),
    "year_of_birth": Field(None, None, True, True, True, True, None, None, None),
}


def age(self):
    return datetime.now().year - self.year_of_birth


MetaPerson = dataclass(type("MetaPerson", (), {"__annotations__": params, "wiekosoby": property(age)}))
