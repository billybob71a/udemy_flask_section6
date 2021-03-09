from db import db
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = True
    db.init_app(app)
    return app


class B(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    @classmethod
    def find_by_name(cls, name):
        print(name)
        item = cls.query.filter_by(name=name).first()
        item.
        print("the item type is")
        return item


if __name__ == '__main__':
    app = create_app()
    app.app_context().push()
    val1 = B.find_by_name(name='test')
    from time import sleep
    sleep(30)
    print("the type of {}".format(type(val1)))
    print(val1.name)