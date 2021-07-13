from flask import Flask, session
from flask import render_template, request, url_for
import database

app = Flask(__name__)
database.CreateTableUser()
database.CreateTableProduct()
app.secret_key = "08859V.P.71086"

@app.route('/')
def home():
    return render_template("home.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        login = database.Login(username, password)
        if login == 1:
            session["email"] = username
            return logged_in()
        else:
            return render_template("login.html", message=login, username=username, password=password)

    return render_template("login.html", message="", username="", password="")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        number = request.form.get("number")
        email = request.form.get("email")
        password = request.form.get("password")
        repassword = request.form.get("repassword")

        if password == repassword:
            accounts = database.getAccounts()
            for x in accounts:
                if x[0] == email:
                    message = "ТОЗИ ИМЕЙ Е ЗАЕТ!"
                    return render_template("register.html", message1=message, message2="", message3="", username=username, number=number, email=email, password=password, repassword=repassword)
                if x[1] == number:
                    message = "ТОЗИ НОМЕР Е ЗАЕТ!"
                    return render_template("register.html", message1="", message2=message, message3="", username=username, number=number, email=email, password=password, repassword=repassword)
            database.Register(username, email, number, repassword)
            return render_template("login.html", message="")
        else:
            message = "ДВЕТЕ ПАРОЛИ НЕ СЪВПАДАТ!"
            return render_template("register.html", message1="", message2="", message3=message, username=username, number=number, email=email, password=password, repassword=repassword)
    return render_template("register.html", message1="", message2="", message3="", username="", number="", email="", password="", repassword="")

@app.route("/logged_in")
def logged_in():
    email = session["email"]
    username = database.getUsername(email)
    return render_template("logged_in.html", username=username)


@app.route("/profile")
def profile():
    info = database.getAccountInfo(session["email"])
    if info[3] is None:
        return render_template("Profile.html", username=info[1], email=info[2], number="-")
    else:
        return render_template("Profile.html", username=info[1], email=info[2], number=info[3])


@app.route("/editProfile", methods=["GET", "POST"])
def editProfile():
    info = database.getAccountInfo(session["email"])
    if request.method == "POST":
        username = request.form.get("username")
        number = request.form.get("number")
        email = request.form.get("email")
        password = request.form.get("password")
        repassword = request.form.get("repassword")

        if password == repassword:
            accounts = database.getAccounts()
            for x in accounts:
                if x[0] == email and email != info[2]:
                    message = "ТОЗИ ИМЕЙ Е ЗАЕТ!"
                    return render_template("EditProfile.html", message1=message, message2="", message3="", username=username, number=number, email=email, password=password, repassword=repassword)
                if x[1] == number and number != info[3]:
                    message = "ТОЗИ НОМЕР Е ЗАЕТ!"
                    return render_template("EditProfile.html", message1="", message2=message, message3="", username=username, number=number, email=email, password=password, repassword=repassword)
            database.deleteAccount(info[2])
            database.Register(username, email, number, repassword)
            session["email"] = email
            return render_template("Profile.html", username=username, email=email, number=number)
        else:
            message = "ДВЕТЕ ПАРОЛИ НЕ СЪВПАДАТ!"
            return render_template("EditProfile.html", message1="", message2="", message3=message, username=username, number=number, email=email, password=password, repassword=repassword)
    return render_template("EditProfile.html", username=info[1], email=info[2], number=info[3], password=info[4], repassword=info[4], message1="", message2="", message3="")


@app.route('/products/chairs')
def Chairs():
    username = database.getUsername(session["email"])
    products = database.getProducts('chair')
    return render_template("Products.html", username=username, products=products, category='СТОЛОВЕ')


@app.route('/products/tables')
def Tables():
    username = database.getUsername(session["email"])
    products = database.getProducts('table')
    return render_template("Products.html", username=username, products=products, category='МАСИ И СТОЛОВЕ')


@app.route('/products/kitchens')
def Kitchens():
    username = database.getUsername(session["email"])
    products = database.getProducts('kitchen')
    return render_template("Products.html", username=username, products=products, category='КУХНИ')


@app.route('/products/wardrobes')
def Wardrobes():
    username = database.getUsername(session["email"])
    products = database.getProducts('wardrobe')
    return render_template("Products.html", username=username, products=products, category='ГАРДЕРОБИ')


@app.route('/products/beds')
def Beds():
    username = database.getUsername(session["email"])
    products = database.getProducts('bed')
    return render_template("Products.html", username=username, products=products, category='ЛЕГЛА')


@app.route("/logout")
def logout():
    session.pop('email', None)
    return render_template("home.html")


if __name__ == '__main__':
    app.run()
