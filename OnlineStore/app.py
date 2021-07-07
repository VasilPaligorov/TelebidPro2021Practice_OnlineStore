from flask import Flask
from flask import render_template, request, url_for
import database

app = Flask(__name__)
database.CreateTablePerson()

@app.route('/')
def home():
    return render_template("home.html")

@app.route("/login", methods=["GET", "POST"])
def check():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        login = database.Login(username, password)

        if login == 1:
            return render_template("home.html")
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
                    message = "This email is taken!"
                    return render_template("register.html", message1=message, message2="", message3="")
                if x[1] == number:
                    message = "This number is taken!"
                    return render_template("register.html", message1="", message2=message, message3="")
            database.Register(username, email, number, repassword)
            return render_template("home.html")
        else:
            message = "Both passwords don't match!"
            return render_template("register.html", message1="", message2="", message3=message)
    return render_template("register.html", message1="", message2="", message3="")


if __name__ == '__main__':
    app.run()
