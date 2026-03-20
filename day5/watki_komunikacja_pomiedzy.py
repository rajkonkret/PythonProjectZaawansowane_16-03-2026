import threading
import queue
import time

data_queue = queue.Queue()


def producer():
    for i in range(5):
        item = f"item {i}"
        print(f"Producent: produkuję: {item}")
        data_queue.put(item)
        time.sleep(1)


def consumer():
    while True:
        item = data_queue.get()
        if item is None:
            break
        print(f"Konsument: odbieram {item}")
        time.sleep(2)
        data_queue.task_done()


producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

producer_thread.join()

data_queue.put(None)
consumer_thread.join()

print("Koniec komunikacji między wątkami")
