import sqlite3
#1.uzdevums
conn=sqlite3.connect('bibloteka.db')


#2.uzdevums
'''conn.execute(CREATE TABLE Gramatas
             (gramatas_id INT PRIMARY KEY    NOT NULL,
             nosaukums       TEXT    NOT NULL,
             gads        INT NOT NULL,
             autora_id    INT);)'''

'''conn.execute(CREATE TABLE Autori
             (autora_id INT PRIMARY KEY    NOT NULL,
             vards       TEXT    NOT NULL,
             uzvards        TEXT NOT NULL);)

conn.commit()

conn.execute("INSERT INTO Gramatas (gramatas_id, nosaukums, gads, autora_id) \
             VALUES(4, 'Rieksti4', 1996, 1)")

conn.commit()'''

#3.uzdevums


cursor = conn.execute("SELECT * FROM Gramatas")
for i in cursor:
    print(i)


all = conn.execute("SELECT * from Gramatas \
                    JOIN Autori on Gramatas.autora_id = Autori.autora_id")
for a in all:
    print(a)


year = conn.execute("SELECT gads from Gramatas \
                    ORDER BY gads")
for a in year:
    print(a)

starta = conn.execute("SELECT * from Gramatas \
                      WHERE nosaukums LIKE 'r%'")
for u in starta:
    print(u)