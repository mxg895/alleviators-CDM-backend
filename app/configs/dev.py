import os
ENV = 'development'
DEBUG = True
DATABASE_URI = 'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
    dbuser=os.environ['DBUSER_DEV'],
    dbpass=os.environ['DBPASS_DEV'],
    dbhost=os.environ['DBHOST_DEV'],
    dbname=os.environ['DBNAME_DEV']
)