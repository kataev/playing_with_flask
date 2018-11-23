import os

from app import create_app
from flask_script import Manager

# To upgrade requirements.txt, use pipreqs

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)

if __name__ == '__main__':
    manager.run()
    # args: runserver -d -p 5001
