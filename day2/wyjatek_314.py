# inne działanie od python 3.14

def h(x):
    try:
        return 10 / x
    except ZeroDivisionError:
        return "coś"
        # print("Coś")
    finally:
        return 123
        # print()

#  SyntaxWarning: 'return' in a 'finally' block
#   return 123

print(h(10))
print(h(0))
# 123
# 123
