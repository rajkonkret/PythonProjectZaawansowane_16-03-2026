class FileManager:
    def __init__(self, filename, mode, encod):
        self.filename = filename
        self.mode = mode
        self.encod = encod
        self.field = None

    def __enter__(self):
        self.file = open(self.filename, self.mode, encoding=self.encod)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with FileManager('test.txt', "w", 'utf-8') as f:
    f.write("To jest pierwsza linia tekstu")

print(f.closed)  # True

w = open("abc.txt", 'w', encoding="utf-8")
w.write("Plik abc...")
w.close()
print(w.closed)  # True

with open("abc.txt", "a", encoding="utf-8") as f:
    f.write("dsfsfhdjshjdshgsjfg\n")

print(f.closed)  # True
