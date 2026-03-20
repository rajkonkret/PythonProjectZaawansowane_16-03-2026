import asyncio
import random
import colorama

# http://en.wikipedia.org/wiki/ANSI_escape_code
c = (
    "\033[0m",
    "\033[36m",
    "\033[91m",
    "\033[35m",
    "\033[33m",
    "\033[92m",
)


async def make_random(idx: int, threshold: int = 6) -> int:
    print(f"{c[idx + 1]} inicjacja make_random({idx})")
    i = random.randint(0, 10)
    while i <= threshold:
        print(f"{c[idx + 1]} make_random({idx}) == {i} -> zbyt niska wartość. Powtarzam")
        await  asyncio.sleep(idx + 1)
        i = random.randint(0, 10)
    print(f"{c[idx + 1]} zakończono make_random({idx}) == {i} {c[0]}.")
    return i


async def main():
    res = await  asyncio.gather(*(make_random(i, 9 - i) for i in range(5)))
    return res


if __name__ == '__main__':
    random.seed(444)
    r1, r2, r3, r4, r5 = asyncio.run(main())
    print(f"\nWyniki: {r1=}, {r2=}, {r3=}, {r4=}, {r5}")
