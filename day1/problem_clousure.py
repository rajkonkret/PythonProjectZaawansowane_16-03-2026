def outer():
    x = []

    def inner(value):
        x.append(value)
        print(x)

    return inner


f = outer()
f(1)  # [1]
f(2)  # [1, 2]
f(3)  # [1, 2, 3]

print(f.__closure__)
# (<cell at 0x0000029D0DB0A5C0: list object at 0x0000029D0D32CFC0>,)
for cell in f.__closure__:
    print(cell.cell_contents)  # [1, 2, 3]
