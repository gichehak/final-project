from flask_script import Manager
from final_project import app, db, Customer, Order

manager = Manager(app)


# reset the database and create two artists
@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    thomas_Trinter = Customer(name='Thomas Trinter', address='1111')
    clinton_White = Customer(name='Clinton White', address='2222')
    mark_Serva = Customer(name='Mark Serva', address='3333')
    edward_Hortono = Customer(name='Edward Hortono', address='4444')
    db.session.add(clinton_White)
    db.session.add(thomas_Trinter)
    db.session.add(mark_Serva)
    db.session.add(edward_Hortono)
    db.session.commit()


if __name__ == "__main__":
    manager.run()
