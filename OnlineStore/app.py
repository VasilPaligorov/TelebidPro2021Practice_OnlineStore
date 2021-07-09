from flask import Flask, session
from flask import render_template, request, url_for
import database

app = Flask(__name__)
database.CreateTablePerson()
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
            return render_template("login.html", message=login)

    return render_template("login.html", message="")

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
                    return render_template("register.html", message1=message, message2="", message3="")
                if x[1] == number:
                    message = "ТОЗИ НОМЕР Е ЗАЕТ!"
                    return render_template("register.html", message1="", message2=message, message3="")
            database.Register(username, email, number, repassword)
            return render_template("login.html", message="")
        else:
            message = "ДВЕТЕ ПАРОЛИ НЕ СЪВПАДАТ!"
            return render_template("register.html", message1="", message2="", message3=message)
    return render_template("register.html", message1="", message2="", message3="")

@app.route("/logged_in")
def logged_in():
    email = session["email"]
    username = database.getUsername(email)
    return render_template("logged_in.html", username=username)


@app.route("/profile")
def profile():
    email = session["email"]
    info = database.getAccountInfo(email)

    if info[3] is None:
        return render_template("Profile.html", username=info[1], email=info[2], number="-")
    else:
        return render_template("Profile.html", username=info[1], email=info[2], number=info[3])


if __name__ == '__main__':
    app.run()
