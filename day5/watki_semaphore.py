import threading
import time
import random

semaphore = threading.Semaphore(3)


def access_resource(thread_id):
    print(f"Wątek {thread_id} czeka na dostęp do zasobu...")
    semaphore.acquire()
    try:
        print(f"Wątek {thread_id} uzyskał dostęp do zasobu...")
        time_to_sleep = random.uniform(1, 3)
        time.sleep(time_to_sleep)
        print(f"Wątek {thread_id} zwalnia zasób po {time_to_sleep} sekund")
    finally:
        semaphore.release()


threads = []
for i in range(10):
    t = threading.Thread(target=access_resource, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Wszystkie wątki zostały zakończone")
