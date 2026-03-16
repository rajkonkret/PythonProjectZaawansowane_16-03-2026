def fibonaci_prime_generator(limit=None):
    """
    Generator liczb fibonacciego, które są liczbami pierwszymi
    :param limit: Opcjonalny limit ilości wygenerowanych liczb.
    :type limit: int or None
    :yield: Kolejna liczba Fibonacciego, będąca liczbą pierwszą
    :rtype: int
    :return:
    """

    a, b = 0, 1
    count = 0

    def is_prime(n):

        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:  # modulo, reszta z dzielenia
                return False
        return True

    while True:
        a, b = b, a + b
        if is_prime(a):
            yield a
            count += 1
            if limit is not None and count >= limit:
                break


generator = fibonaci_prime_generator(limit=5)

for prime in generator:
    print(prime)
# 2
# 3
# 5
# 13
# 89
