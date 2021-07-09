import sqlite3

con = sqlite3.connect('database.db', check_same_thread=False)
cur = con.cursor()

def CreateTablePerson():
    try:
        cur.execute('''create table Person (id integer auto_increment primary key, Username varchar(16) not null, Email text not null unique , Number text unique , Password varchar(8) not null);''')
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

def getUsername(email):
    try:
        int(email)
        cur.execute('''select Username from Person where Number=?''', (email,))
    except:
        cur.execute('''select Username from Person where Email=?''', (email,))

    username = cur.fetchone()
    for x in username:
        print(x)
    return username[0]

def getAccountInfo(email):
    try:
        int(email)
        cur.execute('''select * from Person where Number=?''', (email,))
    except:
        cur.execute('''select * from Person where Email=?''', (email,))

    account = cur.fetchone()
    return account
