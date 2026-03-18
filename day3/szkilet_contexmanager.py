class ContexManager:
    def __init__(self):
        print("Inicjalizacja metody __init__()")

    def __enter__(self):
        # print(5 / 0) nie wykona się __exit__
        print("Inicjalizacja metody __enter__()")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Inicjacja metody __exit__()")


with ContexManager() as manager:
    print("Działanie wewnętrznej instrukcji with...")
    # raise ValueError
# Inicjalizacja metody __init__()
# Inicjalizacja metody __enter__()
# Działanie wewnętrznej instrukcji with...
# Inicjacja metody __exit__()
