import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database/sounding-rocket-history.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'database/db_repository')
SECRET_KEY = 'NmVhNzU0ZmZjYmI3ZjNmODdkYTgwZGFk'

