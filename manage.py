from flask_script import Manager
from final_project import app, db, Customer, Order

manager = Manager(app)


# reset the database and create two artists
@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    thomas_Trinter = Customer(name='Thomas Trinter', address='123 Melbourne, Melbourne, FL 32904')
    clinton_White = Customer(name='Clinton White', address='4 Golfield Rd, Orlando, FL 32806')
    mark_Serva = Customer(name='Mark Serva', address='71 Pilgrim Ave, Chevy Chase, MD 20815 ')
    edward_Hortono = Customer(name='Edward Hortono', address='44 Magnolia St., Newark, DE 19713')
    order1 = Order(name='Order123', year=2015, description=".", customer=mark_Serva)
    order2 = Order(name='Order222', year=2017, description=".", customer=thomas_Trinter)
    db.session.add(clinton_White)
    db.session.add(thomas_Trinter)
    db.session.add(mark_Serva)
    db.session.add(edward_Hortono)
    db.session.add(order1)
    db.session.add(order2)
    db.session.commit()


if __name__ == "__main__":
    manager.run()
