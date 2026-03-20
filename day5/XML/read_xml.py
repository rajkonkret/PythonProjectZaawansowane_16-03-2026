import xml.etree.ElementTree as ET

try:
    tree = ET.parse('subaru_komis.xml')
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
