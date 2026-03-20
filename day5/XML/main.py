from xml.etree.ElementTree import Element, SubElement
import xml.etree.ElementTree as ET
from pretify import pretty

top = Element('autokomis')

# pierwszy samochód
sam1 = SubElement(top, 'samochod')

id = SubElement(sam1, "id")
id.text = 'sam1'

marka = SubElement(sam1, 'marka')
marka.text = 'Subaru'

model = SubElement(sam1, 'model')
model.text = 'Impreza'

poj = SubElement(sam1, 'pojemosc')
poj.text = '2.0'

rocznik = SubElement(sam1, "rocznik")
rocznik.text = '2000'

cena = SubElement(sam1, 'cena')
cena.text = '64000'

wyp_dod = SubElement(sam1, 'wyposazenie_dod')

kolor = SubElement(wyp_dod, 'kolor')
kolor.text = 'czarna perła'

klima = SubElement(wyp_dod, "klimatyzacja")
klima.text = "jest"

print(top)
print(pretty(top))

with open("subaru_komis.xml", "w", encoding='utf-8') as f:
    f.write(pretty(top))