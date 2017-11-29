import os
from flask import Flask, session, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to get secure key'

# setup SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
db = SQLAlchemy(app)


# # define database tables
# class Artist(db.Model):
#     __tablename__ = 'customers'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64))
#     about = db.Column(db.Text)
#     orders = db.relationship('Song', backref='artist')
#
# class Song(db.Model):
#     __tablename__ = 'orders'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(256))
#     year = db.Column(db.Integer)
#     lyrics = db.Column(db.Text)
#     artist_id = db.Column(db.Integer, db.ForeignKey('customers.id'))

@app.route('/')
def index():
    # return HTML
    # return "<h1>this is the index page!<h1>"
    return render_template('index.html')


@app.route('/customers')
def show_all_customers():
    customers = Customer.query.all()
    return render_template('customer-all.html', customers=customers)

# @app.route('/artist/add', methods=['GET', 'POST'])
# def add_customers():
#     if request.method == 'GET':
#         return render_template('artist-add.html')
#     if request.method == 'POST':
#         # get data from the form
#         name = request.form['name']
#         about = request.form['about']
#
#         # insert the data into the database
#         artist = Artist(name=name, about=about)
#         db.session.add(artist)
#         db.session.commit()
#         return redirect(url_for('show_all_customers'))

    # @app.route('/artist/edit/<int:id>', methods=['GET', 'POST'])
    # def edit_artist(id):
    #     artist = Artist.query.filter_by(id=id).first()
    #     if request.method == 'GET':
    #         return render_template('artist-edit.html', artist=artist)
    #     if request.method == 'POST':
    #         # update data based on the form data
    #         artist.name = request.form['name']
    #         artist.about = request.form['about']
    #         # update the database
    #         db.session.commit()
    #         return redirect(url_for('show_all_customers'))

# @app.route('/song/add', methods=['GET', 'POST'])
# def add_orders():
#     if request.method == 'GET':
#         customers = Artist.query.all()
#         return render_template('song-add.html', customers=customers)
#     if request.method == 'POST':
#         # get data from the form
#         name = request.form['name']
#         year = request.form['year']
#         lyrics = request.form['lyrics']
#         artist_name = request.form['artist']
#         artist = Artist.query.filter_by(name=artist_name).first()
#         song = Song(name=name, year=year, lyrics=lyrics, artist=artist)
#
#         # insert the data into the database
#         db.session.add(song)
#         db.session.commit()
#         return redirect(url_for('show_all_orders'))


@app.route('/orders')
def show_all_orders():
    orders = Order.query.all()
    return render_template('order-all.html', orders=orders)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':

    # activates the debugger and the reloader during development
    # app.run(debug=True)
    app.run()

    # make the server publicly available on port 80
    # note that Ports below 1024 can be opened only by root
    # you need to use sudo for the following conmmand
    # app.run(host='0.0.0.0', port=80)
