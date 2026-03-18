class PositiveTuple(tuple):

    def __new__(cls, *numbers):
        skipped = 0
        pos_number = []
        for x in numbers:
            if x >= 0:
                pos_number.append(x)
            else:
                skipped += 1
        instance = super().__new__(cls, pos_number)
        instance._skipped = skipped
        return instance


posnb = PositiveTuple(9, 6, 22, 5, 0, -3, -45, 3, 46, 79, -64, -2, 6, -99)
print(type(posnb))
print(posnb)  # (9, 6, 22, 5, 0, 3, 46, 79, 6)
