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


#  define database tables
class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    address = db.Column(db.Text)
    orders = db.relationship('Order', backref='customer', cascade="delete")


class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    year = db.Column(db.Integer)
    desctription = db.Column(db.Text)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))


@app.route('/')
def index():
    # return HTML
    # return "<h1>this is the index page!<h1>"
    return render_template('index.html')


@app.route('/customers')
def show_all_customers():
    customers = Customer.query.all()
    return render_template('customer-all.html', customers=customers)


@app.route('/customer/add', methods=['GET', 'POST'])
def add_customers():
    if request.method == 'GET':
        return render_template('customer-add.html')
    if request.method == 'POST':
        # get data from the form
        name = request.form['name']
        address = request.form['address']

        # insert the data into the database
        customer = Customer(name=name, address=address)
        db.session.add(customer)
        db.session.commit()
        return redirect(url_for('show_all_customers'))


@app.route('/api/customer/add', methods=['POST'])
def add_ajax_customers():
    # get data from the form
    name = request.form['name']
    address = request.form['address']

    # insert the data into the database
    customer = Customer(name=name, address=address)
    db.session.add(customer)
    db.session.commit()
    # flash message type: success, info, warning, and danger from bootstrap
    flash('Customer Inserted', 'success')
    return jsonify({"id": str(customer.id), "name": customer.name})


@app.route('/customer/edit/<int:id>', methods=['GET', 'POST'])
def edit_customers(id):
    customer = Customer.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('customer-edit.html', customer=customer)
    if request.method == 'POST':
        # update data based on the form data
        customer.name = request.form['name']
        customer.address = request.form['address']
        # update the database
        db.session.commit()
        return redirect(url_for('show_all_customers'))


@app.route('/customer/delete/<int:id>', methods=['GET', 'POST'])
def delete_customer(id):
    customer = Customer.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('customer-delete.html', customer=customer)
    if request.method == 'POST':
        # delete the artist by id
        # all related songs are deleted as well
        db.session.delete(customer)
        db.session.commit()
        return redirect(url_for('show_all_customers'))


@app.route('/api/customer/<int:id>', methods=['DELETE'])
def delete_ajax_customer(id):
    customer = Customer.query.get_or_404(id)
    db.session.delete(customer)
    db.session.commit()
    return jsonify({"id": str(customer.id), "name": customer.name})


@app.route('/orders')
def show_all_orders():
    orders = Order.query.all()
    return render_template('order-all.html', orders=orders)


@app.route('/order/add', methods=['GET', 'POST'])
def add_orders():
    if request.method == 'GET':
        customers = Customer.query.all()
        return render_template('order-add.html', customers=customers)
    if request.method == 'POST':
        # get data from the form
        name = request.form['name']
        year = request.form['year']
        desctription = request.form['desctription']
        customer_name = request.form['customer']
        customer = Customer.query.filter_by(name=customer_name).first()
        order = Order(name=name, year=year, desctription=desctription, customer=customer)

        # insert the data into the database
        db.session.add(order)
        db.session.commit()
        return redirect(url_for('show_all_orders'))


@app.route('/order/edit/<int:id>', methods=['GET', 'POST'])
def edit_order(id):
    order = Order.query.filter_by(id=id).first()
    customers = Customer.query.all()
    if request.method == 'GET':
        return render_template('order-edit.html', order=order, customers=customers)
    if request.method == 'POST':
        # update data based on the form data
        order.name = request.form['name']
        order.year = request.form['year']
        order.desctription = request.form['desctription']
        customer_name = request.form['customer']
        customer = Customer.query.filter_by(name=customer_name).first()
        order.customer = customer
        # update the database
        db.session.commit()
        return redirect(url_for('show_all_orders'))


@app.route('/order/delete/<int:id>', methods=['GET', 'POST'])
def delete_order(id):
    order = Order.query.filter_by(id=id).first()
    customers = Customer.query.all()
    if request.method == 'GET':
        return render_template('order-delete.html', order=order, customers=customers)
    if request.method == 'POST':
        # use the id to delete the song
        # song.query.filter_by(id=id).delete()
        db.session.delete(order)
        db.session.commit()
        return redirect(url_for('show_all_orders'))


@app.route('/api/order/<int:id>', methods=['DELETE'])
def delete_ajax_order(id):
    order = Order.query.get_or_404(id)
    db.session.delete(order)
    db.session.commit()
    return jsonify({"id": str(order.id), "name": order.name})


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/order/<int:id>/')
def get_order_id(id):
    # return "This order's ID is " + str(id)
    return "Hi, this is %s and the order's id is %d" % ('administrator', id)


if __name__ == '__main__':

    # activates the debugger and the reloader during development
    # app.run(debug=True)
    app.run()

    # make the server publicly available on port 80
    # note that Ports below 1024 can be opened only by root
    # you need to use sudo for the following conmmand
    # app.run(host='0.0.0.0', port=80)
