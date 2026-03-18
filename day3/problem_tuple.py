# tupla jest niemutowalna
# nie da się zmienić działania tupli z pythona nadpisując __init__

# class Point(tuple):
#     def __init__(self, x, y):
#         self[0] = x
#         self[1] = y
#
#
# ob = Point(1, 2)  # TypeError: tuple expected at most 1 argument, got 2


class Point(tuple):
    def __init__(self, x, y):
        self.x = x
        self.y = y

#
# # ob = Point(1,2)
# ob = Point(1) # TypeError: 'int' object is not iterable
