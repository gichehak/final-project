import os
from flask import Flask, session, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to get secure key'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# setup SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
db = SQLAlchemy(app)


# # define database tables
# class Customer(db.Model):
#     __tablename__ = 'customers'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64))
#     address = db.Column(db.Text)
#     orders = db.relationship('Order', backref='customer')
#
# class Order(db.Model):
#     __tablename__ = 'orders'
#     id = db.Column(db.Integer, primary_key=True)
#     description = db.Column(db.String(256))
#     order_date = db.Column(db.Integer)
#     customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))

@app.route('/')
def index():
    # return HTML
    # return "<h1>this is the index page!<h1>"
    return render_template('index.html')


@app.route('/customers')
def show_all_customers():
    customers = Customer.query.all()
    return render_template('customer-all.html', customers=customers)

# @app.route('/customer/add', methods=['GET', 'POST'])
# def add_customers():
#     if request.method == 'GET':
#         return render_template('customer-add.html')
#     if request.method == 'POST':
#         # get data from the form
#         name = request.form['name']
#         about = request.form['about']
#
#         # insert the data into the database
#         customer = Customer(name=name, about=about)
#         db.session.add(customer)
#         db.session.commit()
#         return redirect(url_for('show_all_customers'))

    # @app.route('/customer/edit/<int:id>', methods=['GET', 'POST'])
    # def edit_customers(id):
    #     customer = Customer.query.filter_by(id=id).first()
    #     if request.method == 'GET':
    #         return render_template('customer-edit.html', customer=customer)
    #     if request.method == 'POST':
    #         # update data based on the form data
    #         customer.name = request.form['name']
    #         customer.about = request.form['about']
    #         # update the database
    #         db.session.commit()
    #         return redirect(url_for('show_all_customers'))

# @app.route('/order/add', methods=['GET', 'POST'])
# def add_orders():
#     if request.method == 'GET':
#         customers = Customer.query.all()
#         return render_template('order-add.html', customers=customers)
#     if request.method == 'POST':
#         # get data from the form
#         name = request.form['name']
#         year = request.form['year']
#         lyrics = request.form['lyrics']
#         customer_name = request.form['customer_name']
#         customer = Customer.query.filter_by(name=customer_name).first()
#         order = Order(name=name, year=year, lyrics=lyrics, customer=customer)
#
#         # insert the data into the database
#         db.session.add(order)
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
