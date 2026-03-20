import asyncio
import time
import httpx

url = "https://api.nbp.pl/api/exchangerates/rates/A/EUR/"


async def fetch_data(client, url, index):
    start_time = time.time()
    response = await client.get(url)
    elapsed_time = time.time() - start_time
    print(f"Request {index}: Status {response.status_code}, Time {elapsed_time:.4f} s")

    try:
        json_data = response.json()
        print(f"Request {index}: Data {json_data}")
    except httpx.HTTPStatusError:
        print(f"Request {index}: Failed with status {response.status_code}")
    except Exception as e:
        print(f"Request {index}: Error {e}")


async def multiple_httpx():
    start_time = time.time()
    async with httpx.AsyncClient() as client:
        tasks = [fetch_data(client, url, i + 1) for i in range(1)]
        await asyncio.gather(*tasks)

    elapsed_time = time.time() - start_time
    print(f"HTTPX total time: {elapsed_time:.4f} s")


asyncio.run(multiple_httpx())
# Request 1: Status 200, Time 0.0504 s
# Request 1: Data {'table': 'A', 'currency': 'euro', 'code': 'EUR', 'rates': [{'no': '055/A/NBP/2026', 'effectiveDate': '2026-03-20', 'mid': 4.2768}]}
# HTTPX total time: 0.4996 s dla 1 zadania
# HTTPX total time: 1.8734 s dla 100 zadań
