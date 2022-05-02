#!/usr/bin/env python3.8

from flask_script import Manager, Server
from app import create_app

#creating app instance

app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server)

if __name__ == '__main__':
    manager.run()

