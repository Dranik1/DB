import sqlite3

conn = sqlite3.connect('test.db')
print('Datu bāze ir izveidota')

'''conn.execute(CREATE TABLE COMPANY
             (ID INT PRIMARY KEY    NOT NULL,
             NAME       TEXT    NOT NULL,
             AGE        INT NOT NULL,
             ADDRESS    CHAR(50),
             SALARY     REAL);)



print("Tabula ir izveidota!")'''

'''conn.execute(INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY)  
             VALUES(1, 'Paul', 32, 'California', 20000.0))

conn.execute(INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY)  
             VALUES(2, 'Alex', 25, 'Latvia', 15000.0))

conn.execute(INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY)  
             VALUES(3, 'Teddy', 23, 'Norway', 20000.0))

conn.execute(INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY)  
             VALUES(4, 'Mark', 25, 'Germany', 65000.0))

conn.commit()'''

cursor = conn.execute("SELECT * from COMPANY")
for i in cursor:
    print(i)




conn.close()