from flask_script import Manager
from final_project import app, db

manager = Manager(app)

if __name__ == "__main__":
    manager.run()
