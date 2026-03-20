import xml.etree.ElementTree as ET

try:
    # tree = ET.parse('subaru_komis.xml')
    tree = ET.parse('kraj.xml')
    root = tree.getroot()

    for child in root:
        print(f"tag: {child.tag}, atrybuty: {child.attrib}")

    print(root[0])
    print(root[0][1])
    print(root[0][1].text)
except Exception as e:
    print("Bład:", e)
# tag: samochod, atrybuty: {}
# tag: samochod, atrybuty: {}
# <Element 'samochod' at 0x000001F235118EF0>
# <Element 'marka' at 0x000001F235118F90>
# Subaru

#
# tag: country, atrybuty: {'name': 'Liechtenstein', 'continent': 'Europa'}
# tag: country, atrybuty: {'name': 'Panama', 'continent': 'Ameryka Środkowa'}
# tag: country, atrybuty: {'name': 'Polska', 'continent': 'Europa'}
# <Element 'country' at 0x000001FDF7948EF0>
# <Element 'rok' at 0x000001FDF7948F90>
# 2020