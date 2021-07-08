import sqlite3

con = sqlite3.connect('database.db', check_same_thread=False)
cur = con.cursor()

def CreateTablePerson():
    try:
        cur.execute('''create table Person (id integer auto_increment primary key, Username varchar(16) not null, Email varchar(45) not null unique , Number varchar(15) unique , Password varchar(8) not null);''')
    except:
        pass

def getAccounts():
    cur.execute('''select Email, Number from Person''')
    accounts = cur.fetchall()
    return accounts

def Register(Username, Email, Number, Password):
    if Number:
        cur.execute('insert into Person(Username, Email, Number, Password) values ("' + Username + '","' + Email + '","' + Number + '","' + Password + '")')
    else:
        cur.execute('insert into Person(Username, Email, Password) values ("' + Username + '","' + Email + '","' + Password + '")')
    con.commit()

def Login(Username, Password):
    try:
        int(Username)
        cur.execute('''select Number, Password from Person''')
        accounts = cur.fetchall()
    except:
        cur.execute('''select Email, Password from Person''')
        accounts = cur.fetchall()

    for x in accounts:
        if x[0] == Username and x[1] == Password:
            return 1

    for x in accounts:
        if x[0] == Username:
            return "ГРЕШНА ПАРОЛА!"

    return "АКАУНТЪТ НЕ Е НАМЕРЕН!"