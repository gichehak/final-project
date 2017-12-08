from flask_script import Manager
from final_project import app, db, Customer, Order

manager = Manager(app)


# reset the database and create two artists
@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    thomas_Trinter = Customer(name='Thomas Trinter', address='123 Melbourne, Melbourne, FL 32904')
    clinton_White = Customer(name='Clinton White', address='4 Golfield Rd., Orlando, FL 32806')
    mark_Serva = Customer(name='Mark Serva', address='71 Pilgrim Ave., Chevy Chase, MD 20815')
    edward_Hortono = Customer(name='Edward Hortono', address='44 Magnolia St., Newark, DE 19713')
    rob_Spotts = Customer(name='Rob Spotts', address='616 Sierra Dr., Evans, GA 30809')
    xiao_Fang = Customer(name='Xiao Fang', address='37 Summer Court, Fairfax, VA 22030')
    harry_Wang = Customer(name='Harry Wang', address='7 South Ohio Rd., Garden City, NY 11530')
    order1 = Order(name='Order123', year=2015, description="Tablet, screen protector, protective case.", customer=mark_Serva)
    order2 = Order(name='Order222', year=2016, description="Laptop, headphones.", customer=thomas_Trinter)
    order3 = Order(name='Order252', year=2016, description="Phone, screen protector, bluetooth headphones.", customer=rob_Spotts)
    order4 = Order(name='Order303', year=2017, description="Tablet, headphones.", customer=xiao_Fang)
    order5 = Order(name='Order305', year=2017, description="Desktop computer, wireless mouse.", customer=harry_Wang)
    db.session.add(clinton_White)
    db.session.add(thomas_Trinter)
    db.session.add(mark_Serva)
    db.session.add(edward_Hortono)
    db.session.add(rob_Spotts)
    db.session.add(xiao_Fang)
    db.session.add(harry_Wang)
    db.session.add(order1)
    db.session.add(order2)
    db.session.add(order3)
    db.session.add(order4)
    db.session.add(order5)
    db.session.commit()


if __name__ == "__main__":
    manager.run()
