import csv

fields = []
rows = []

with open("bmw_global_sales_2018_2025.csv") as f:
    dialect = csv.Sniffer().sniff(f.read(1024))
    print(dialect.delimiter)
    print(dialect.quotechar)

    f.seek(0)  # wraca odczyt na początek pliku
    csvreader = csv.reader(f)
    print(csvreader)  # <_csv.reader object at 0x000001A3AA04B520>

    fields = next(csvreader)

    for row in csvreader:
        rows.append(row)

print("Fields:", fields)
print("Rows:", rows)

# print(50 * "-")
# for r in csvreader:
#     print(r) # ValueError: I/O operation on closed file.
