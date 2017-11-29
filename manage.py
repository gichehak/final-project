from flask_script import Manager
from songbase import app, db, Artist,Song

manager = Manager(app)

if __name__ == "__main__":
    manager.run()
