import csv
# from flask_sqlalchemy import SQLAlchemy
import os
import sys
from uuid import UUID

from dotenv import load_dotenv
# from app.resources.model import Resource
from flask import Flask

from app.extensions import cors, db
from app.resources.data import transform_resources
from app.resources.model import *


def create_app():
    app = Flask(__name__, instance_relative_config=False)

    if not 'WEBSITE_HOSTNAME' in os.environ:
        # local development, where we'll use environment variables
        app.config.from_pyfile('configs/dev.py')
    else:
        # production
        app.config.from_pyfile('configs/prod.py')

    app.config.update(
        SQLALCHEMY_DATABASE_URI=app.config.get('DATABASE_URI'),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )
    app.config['CORS_HEADERS'] = 'Content-Type'
    cors.init_app(app, origins=["http://localhost:3000/*"], headers='Content-Type')
    db.init_app(app)
    with app.app_context():
        db.create_all()
        # if len(args := sys.argv) > 2 and app.config.get("ENV") == "development":
        #     try:
        #         with open('data.csv', 'r', encoding='utf-8-sig', newline='') as f:
        #             reader = csv.DictReader(f)
        #             for row in reader:
        #                 resource = Resource(
        #                     id = row['id'],
        #                     title=row['title'],
        #                     description = row['description'],
        #                     content = row['content'],
        #                     aspect = map(lambda val: Aspect[val.strip()], row['aspect'].split(',')),
        #                     goal = map(lambda val: Goal[val.strip()], row['goal'].split(',')),
        #                     sub_category = map(lambda val: SubCategory[val.strip()], row['sub_category'].split(',')),
        #                     image_name = row['image_name'],
        #                     external_links = row['external_links'])
        #                 db.session.add(resource)
        #             db.session.commit()
        #             f.close()
        #     except Exception as e:
        #         print('Error transferring data from data.csv to PostgreSQL db')
        #         print(e)
        @app.route('/')
        def hello():
            return 'Hello World!'
        from app.resources import routes
        app.register_blueprint(routes.resource)

    return app


