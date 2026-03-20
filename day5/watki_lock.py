import threading


def worker(lock, shared_variable):
    lock.acquire()
    try:
        shared_variable[0] += 1
        print(f"Wątek {threading.current_thread().name} zwiększył wartośc zmiennej wspóldzielonej")
    finally:
        lock.release()


shared_variable = [0]
lock = threading.Lock()

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(lock, shared_variable))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"Zmienna współdzielona: {shared_variable}")
# Wątek Thread-1 (worker) zwiększył wartośc zmiennej wspóldzielonej
# Wątek Thread-2 (worker) zwiększył wartośc zmiennej wspóldzielonej
# Wątek Thread-3 (worker) zwiększył wartośc zmiennej wspóldzielonej
# Wątek Thread-4 (worker) zwiększył wartośc zmiennej wspóldzielonej
# Wątek Thread-5 (worker) zwiększył wartośc zmiennej wspóldzielonej
# Zmienna współdzielona: [5]
