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


parser = xml.sax.make_parser()
parser.setFeature(xml.sax.handler.feature_namespaces, 0)

handler = Uchwytfilmu()
parser.setContentHandler(handler)
parser.parse('filmy.xml')
# --- film ---
# Tytuł filmu: Gwiezdne Wojny
# Rok produkcji filmu: 2019
# Kraj produkcji filmu: USA
# Czas trwania filmu: 140
# Gatunek filmu: SF
# --- film ---
# Tytuł filmu: Ostatni Samuraj
# Rok produkcji filmu: 2001
# Kraj produkcji filmu: USA
# Czas trwania filmu: 145
# Gatunek filmu: Historyczny
# --- film ---
# Tytuł filmu: Obecność 2
# Rok produkcji filmu: 2015
# Kraj produkcji filmu: USA
# Czas trwania filmu: 121
# Gatunek filmu: Horror
# --- film ---
# Tytuł filmu: Kameleon
# Rok produkcji filmu: 2011
# Kraj produkcji filmu: USA
# Czas trwania filmu: 98
# Gatunek filmu: Komedia
# --- film ---
# Tytuł filmu: Ogniem i mieczem
# Rok produkcji filmu: 2000
# Kraj produkcji filmu: Polska
# Czas trwania filmu: 178
# Gatunek filmu: Historyczny