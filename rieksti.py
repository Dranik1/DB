import sqlite3

conn = sqlite3.connect('rieksti.db')
cursor = conn.cursor()


'''cursor.execute(
            SELECT
                vards, datums, nosaukums, cena, daudzums
            FROM
               Detalas
            Join
               pasutijums on Detalas.pasutijuma_id = pasutijums.pasutijuma_id
            Join
               Klients on Klients.klienta_id = pasutijums.klienta_id
            Join
               produkts on produkts.produkts_id = Detalas.produkta_id
               )'''


id=int(input())
vards = input()
epasts = input()
tel = input()


cursor.execute('''INSERT INTO Klients (klienta_id, vards, epasts, telefons) VALUES (?, ?, ?, ? )''', (id, vards, epasts, tel))

cursor.execute('''SELECT * FROM Klients''')

orders = cursor.fetchall()
print("Pasutijumi:")
for order in orders:
    print(order)