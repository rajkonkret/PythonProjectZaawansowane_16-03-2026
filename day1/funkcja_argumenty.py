# * dowolna ilość argumentów przekazaych po pozycji
# ** dowolna ilość argumentów przekazaych po nazwie

def all_params(a, b, /, c=10, *args, d=256, **kwargs):
    print(f"{a=}, {b=}, {c=}, {d=}")
    print(args)
    print(kwargs)


# all_params() # TypeError: all_params() missing 2 required positional arguments: 'a' and 'b'

# a=1, b=2, c=10, d=256
# ()
# {}

all_params(1, 2, 3, 4, 5, 6, 7, d=100, p=90)
# a=1, b=2, c=3, d=100
# (4, 5, 6, 7)
# {'p': 90}

# all_params(b=9, 9) # SyntaxError: positional argument follows keyword argument
# / wymusza przekazywanie a i b po pozycji, po nazwie bedzie bład
# all_params(b=9, a=10) # TypeError: all_params() missing 2 required positional arguments: 'a' and 'b'
all_params(1, 2)
all_params(1, 2, c=90)
all_params(1, 2, 90)
all_params(1, 2, 3, 4, 5, 6, 7, d=100, p=90, a=10)


# a=1, b=2, c=3, d=100
# (4, 5, 6, 7)
# {'p': 90, 'a': 10}

def all_params_2(a, b, *, c, d):
    print(a, b, c, d)


# * argumenty po prawej stronie tylko po nazwie
# all_params_2(1, 2, 3, 4) # TypeError: all_params_2() takes 2 positional arguments but 4 were given
all_params_2(1, 2, c=9, d=90)  # 1 2 9 90

age = 90
print("Radek:", age)
# Radek: 90
#  sep
#         string inserted between values, default a space.
#       end
#         string appended after the last value, default a newline.

print("Radek", age, sep=": ")  # Radek: 90
