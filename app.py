from my_bookstore import app, db
from flask import render_template, redirect, url_for
from my_bookstore.forms import AddForm, DelForm
from my_bookstore.models import Book
from flask_login import logout_user
from flask_dance.contrib.google import google

@app.route('/')
def index():
    books = Book.query.all()
    return render_template('home.html', books=books)

@app.route('/welcome')
def welcome_user():
        resp = google.get("/oauth2/v2/userinfo")
        assert resp.ok, resp.text
        email=resp.json()["email"]
        return render_template('home.html', email=email)

@app.route("/login/google")
def login():
    if not google.authorized:
        return render_template(url_for("google.login"))

    resp = google.get("/oauth2/v2/userinfo")
    assert resp.ok, resp.text
    email=resp.json()["email"]

    return render_template("home.html",email=email)

@app.route("/logout")
def logout():
    logout_user()         
    return redirect(url_for('index'))


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data

        new_book = Book(name)
        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for("list"))

    return render_template("add.html", form=form)


@app.route("/list")
def list():
    books = Book.query.all()
    return render_template("list.html", books=books)


@app.route("/delete", methods=["GET", "POST"])
def delete():

    form = DelForm()

    if form.validate_on_submit():
        isbn = form.isbn.data
        book = Book.query.get(isbn)
        db.session.delete(book)
        db.session.commit()

        return redirect(url_for("list"))
    return render_template("delete.html", form=form)



if __name__ == '__main__':
    #port = int(os.environ.get('PORT', 5000))
    app.run(debug=True)