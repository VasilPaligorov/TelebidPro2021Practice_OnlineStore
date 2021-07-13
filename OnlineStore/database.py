import sqlite3

con = sqlite3.connect('database.db', check_same_thread=False)
cur = con.cursor()

def CreateTableUser():
    try:
        cur.execute('''create table User (id integer primary key autoincrement, Username varchar(16) not null, Email text not null unique , Number text unique , Password varchar(8) not null);''')
    except:
        pass

def getAccounts():
    cur.execute('''select Email, Number from User''')
    accounts = cur.fetchall()
    return accounts

def Register(Username, Email, Number, Password):
    if Number:
        cur.execute('insert into User(Username, Email, Number, Password) values ("' + Username + '","' + Email + '","' + Number + '","' + Password + '")')
    else:
        cur.execute('insert into Puser(Username, Email, Password) values ("' + Username + '","' + Email + '","' + Password + '")')
    con.commit()

def Login(Username, Password):
    try:
        int(Username)
        cur.execute('''select Number, Password from User''')
        accounts = cur.fetchall()
    except:
        cur.execute('''select Email, Password from User''')
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
        cur.execute('''select Username from User where Number=?''', (email,))
    except:
        cur.execute('''select Username from User where Email=?''', (email,))

    username = cur.fetchone()
    for x in username:
        print(x)
    return username[0]

def getAccountInfo(email):
    try:
        int(email)
        cur.execute('''select * from User where Number=?''', (email,))
    except:
        cur.execute('''select * from User where Email=?''', (email,))

    account = cur.fetchone()
    return account

def deleteAccount(email):
    account = getAccountInfo(email)
    cur.execute('''delete from User where Email=? ''', (account[2],))
    con.commit()

# <======================================= TABLE PRODUCT =======================================>

def CreateTableProduct():
    try:
        cur.execute('''create table Product (id integer primary key autoincrement, Name TEXT not null, Picture BLOB, Category TEXT not null, Price REAL NOT NULL, Description TEXT not null);''')
        cur.execute('insert into Product(Name, Category, Price, Description) values ("Стол1", "chair", 15.4,"МЕГА ЯК СТОЛ" );')
        cur.execute('insert into Product(Name, Category, Price, Description) values ("Маса§Стол1", "table", 60,"МЕГА ЯКА МАСА. И СТОЛА НЕ Е ЗЛЕ." );')
        cur.execute('insert into Product(Name, Category, Price, Description) values ("КУХНЯ1", "kitchen", 300,"МЕГА ЯКА КУХНЯ" );')
        cur.execute('insert into Product(Name, Category, Price, Description) values ("ГАРДЕРОБ1", "wardrobe", 150,"КАПЕПЕЕЦ" );')
        cur.execute('insert into Product(Name, Category, Price, Description) values ("ЛЕГЛО1", "bed", 1500, "МЕГА ЯКО ЛЕГЛО. ИДВА В КОМПЛЕКТ С МИЯ КАЛИФА." );')

    except:
        pass

def getProducts(category):
    cur.execute('''select * from Product where Category=?''', (category,))
    products = cur.fetchall()
    for product in products:
        print(product[3])
    return products