import os
ENV = 'production'
DEBUG = False
DATABASE_URI = 'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
    dbuser=os.environ['DBUSER'],
    dbpass=os.environ['DBPASS'],
    dbhost=os.environ['DBHOST'] + ".postgres.database.azure.com",
    dbname=os.environ['DBNAME']
)