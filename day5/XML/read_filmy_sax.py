import xml.sax
from ctypes.wintypes import tagRECT


class Uchwytfilmu(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.id = ""
        self.tytul = ""
        self.rok = ""
        self.kraj = ""
        self.czas_t = ""
        self.gatunek = ""

    def startElement(self, tag, attrs):
        self.CurrentData = tag
        if tag == "film":
            print("--- film ---")

    def endElement(self, tag):
        if self.CurrentData == "if_filmu":
            print(f"Identyfikator filmu: {self.id}")
        elif self.CurrentData == "tytul":
            print(f"Tytuł filmu: {self.tytul}")
        elif self.CurrentData == "rok":
            print(f"Rok produkcji filmu: {self.rok}")
        elif self.CurrentData == "kraj":
            print(f"Kraj produkcji filmu: {self.kraj}")
        elif self.CurrentData == "czas_trwania":
            print(f"Czas trwania filmu: {self.czas_t}")
        elif self.CurrentData == "gatunek":
            print(f"Gatunek filmu: {self.gatunek}")

    def characters(self, content):
        if self.CurrentData == "if_filmu":
            self.id = content
        elif self.CurrentData == "tytul":
            self.tytul = content
        elif self.CurrentData == "rok":
            self.rok = content
        elif self.CurrentData == "kraj":
            self.kraj = content
        elif self.CurrentData == "czas_trwania":
            self.czas_t = content
        elif self.CurrentData == "gatunek":
            self.gatunek = content
