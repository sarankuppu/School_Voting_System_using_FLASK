from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)
party3 = 0
party4 = 0

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database='voting'
)
mycursor = mydb.cursor()


@app.route('/')
def home():
    return render_template("vote1.html")


@app.route('/vote', methods=["GET","POST"])
def vote():
    mycursor.execute('INSERT INTO votes VALUES("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")'
                     .format(request.form.get("name"),request.form.get("house"),request.form.get("president"),request.form.get("vice president"),
                             request.form.get("sports minister"),request.form.get("cultural minister"),request.form.get("communication minister"),request.form.get("literacy minister"),
                             request.form.get("Junior Squadron"),request.form.get("Senior Squadron"),request.form.get("House Commander"),request.form.get("Deputy House Commander")))
    mydb.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
