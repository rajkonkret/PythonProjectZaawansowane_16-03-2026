import time
import asyncio
# do zadań i/o bound

async def count():
    print("Start")
    await asyncio.sleep(3.355)
    # time.sleep() - wstrzymałby wątek, pętla nie działa
    print("Koniec")


async def main():
    await asyncio.gather(count(), count(), count())


if __name__ == '__main__':
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter()
    print(f"{__file__} wykonany w czasie {elapsed - s:.2f} s")
# Start
# Start
# Start
# Koniec
# Koniec
# Koniec
# C:\Users\CSComarch\AI\PythonProjectZaawansowane_16-03-2026\day5\watki\asyncio_basic.py wykonany w czasie 3.37 s
