import sqlite3
import random
con = sqlite3.connect('database.db', check_same_thread=False)
cur = con.cursor()


# <======================================= TABLE STUFF =======================================>
def CreateTableStuff():
    try:
        cur.execute('''create table Stuff (id integer primary key autoincrement, Email text not null unique, Password varchar(8) not null);''')
        cur.execute('''insert into Stuff(Email, Password) values ("admin@gmail.com", "admin123");''')
        con.commit()
    except:
        pass

def getStuffAccounts():
    cur.execute('''select Email from Stuff;''')
    accounts = cur.fetchall()
    return accounts


def StuffLogin(Username, Password):
    cur.execute('''select Email, Password from Stuff;''')
    accounts = cur.fetchall()
    for x in accounts:
        if x[0] == Username and x[1] == Password:
            return 1

    for x in accounts:
        if x[0] == Username:
            return "ГРЕШНА ПАРОЛА!"

    return "АКАУНТЪТ НЕ Е НАМЕРЕН!"


# <======================================= TABLE USER =======================================>


def CreateTableUser():
    try:
        cur.execute('''create table User (id integer primary key autoincrement, Username varchar(16) not null, Email text not null unique , Number text unique , Password varchar(8) not null);''')
    except:
        pass

def getAccounts():
    cur.execute('''select Email, Number from User;''')
    accounts = cur.fetchall()
    return accounts

def Register(Username, Email, Number, Password):
    if Number:
        cur.execute('insert into User(Username, Email, Number, Password) values (?,?,?,?);', (Username, Email, Number, Password))
    else:
        cur.execute('insert into User(Username, Email, Password) values (?,?,?);', (Username, Email, Password))
    con.commit()

def Login(Username, Password):
    try:
        int(Username)
        cur.execute('''select Number, Password from User;''')
        accounts = cur.fetchall()
    except:
        cur.execute('''select Email, Password from User;''')
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
        cur.execute('''select Username from User where Number=?;''', (email,))
    except:
        cur.execute('''select Username from User where Email=?;''', (email,))

    username = cur.fetchone()
    return username[0]

def getAccountInfo(email):
    try:
        int(email)
        cur.execute('''select * from User where Number=?;''', (email,))
    except:
        cur.execute('''select * from User where Email=?;''', (email,))

    account = cur.fetchone()
    return account

def deleteAccount(email):
    account = getAccountInfo(email)
    cur.execute('''delete from User where Email=?; ''', (account[2],))
    con.commit()

# <======================================= TABLE PRODUCT =======================================>


def CreateTableProduct():
    try:
        cur.execute('''create table Product (id integer primary key autoincrement, Name TEXT not null, Picture BLOB,
         Category TEXT not null, Price REAL NOT NULL, Description TEXT not null, int cartId, foreign key (cartId) references cart.id);''')

    except:
        pass


def getProducts(category):
    cur.execute('''select * from Product where Category=?;''', (category,))
    products = cur.fetchall()
    return products

def getProductsName():
    cur.execute('''select Name from Product''')
    products = cur.fetchall()
    return products

def addProduct(name, category, price, desc):
    cur.execute('insert into Product (Name, Category, Price, Description) values (?,?,?,?);', (name, category, price, desc))
    con.commit()


def getProductInfo(id):
    try:
        len(id)
        cur.execute('SELECT * FROM Product WHERE id IN (%s)' % ','.join('?' * len(id)), tuple(id))
        info = cur.fetchall()
        return info
    except:
        cur.execute('''select * from Product where id = ?;''', (id, ))
        info = cur.fetchone()
        return info


# <======================================= TABLE CART =======================================>


def CreateTableCart():
    try:
        cur.execute('''create table Cart(id integer primary key autoincrement, Name TEXT not null, ProductId int not null, foreign key(ProductId) references Product(id));''')

    except:
        pass

def addProductToCart(id, name):
    cur.execute('insert into Cart (Name, ProductId) values (?,?);', (name, id))
    con.commit()

def getCart(name):
    cur.execute('''select ProductId from Cart where name =? ''', (name, ))
    ProductsId = cur.fetchall()
    IdList = []
    for x in ProductsId:
        print(x)
        for u in x:
            print(u)
            IdList.append(u)
    print(IdList)
    print(ProductsId)
    return IdList

def removeFromCart(id, name):
    cur.execute('''delete from Cart where Name=? and  ProductId = ? Limit 1; ''', (name, id))
    con.commit()


# <======================================= TABLE ORDER =======================================>

def CreateTableOrder():
    try:
        cur.execute('''create table Orders(id integer primary key autoincrement, PersonName Text not null, Products Text not null);''')

    except:
        pass


def CreateOrder(Pname, PIds):
    a = ""
    for x in PIds:
        a = str(a)+str(x)+" "
    cur.execute('''INSERT INTO Orders (PersonName, Products) VALUES (?, ?)''', (Pname, a))
    con.commit()
    cur.execute('''delete from Cart where Name=?; ''', (Pname, ))
    con.commit()


def getOrders():
    cur.execute('''select * from orders''')
    orders = cur.fetchall()
    return orders