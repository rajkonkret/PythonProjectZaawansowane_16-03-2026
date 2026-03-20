import configparser
import mysql.connector

#ładowanie pliku konfiguracyjnego
config = configparser.ConfigParser()
config.read("config.ini")

#pobranie danych z sekcji [mysql]
db_user = config['mysql']['user']
db_password = config['mysql']['password']
db_host = config['mysql']['host']
db_port = config['mysql']['port']
db_database = config['mysql']['database']

connection = mysql.connector.connect(
    user = db_user,
    password = db_password,
    host = db_host,
    port = db_port,
    database = db_database
)

cursorObject = connection.cursor()

query = "SELECT firstname, lastname FROM student"
cursorObject.execute(query)
print(cursorObject)

wynik = cursorObject.fetchall()
print(wynik)

for x,y in wynik:
    print(f"imię: {x}, nazwisko: {y}")

print("_"*70)

q2 = "SELECT firstname,lastname FROM student WHERE studentid>66000;"

cursorObject.execute(q2)
print(type(cursorObject))
print(cursorObject)

wynik = cursorObject.fetchall()
print(wynik)

# q3 = "SELECT firstname FROM vstud;"
# cursorObject.execute(q3)
#
# wynik = cursorObject.fetchall()
# print(wynik)
