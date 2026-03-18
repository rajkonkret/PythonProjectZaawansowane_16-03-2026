# od 3.10

lang = input("Podaj imię")

match lang.strip().casefold():
    case "radek":
        print("OK")
    case "tomek":
        print("Tomek")
    case _:  # else
        print("inny")

name1 = "GROSS"
name2 = "groß"

print(name1.lower() == name2.lower())  # False
""" Return a version of the string suitable for caseless comparisons. """
print(name1.casefold() == name2.casefold())  # True

# https://www.unicode.org/Public/UCD/latest/ucd/SpecialCasing.txt