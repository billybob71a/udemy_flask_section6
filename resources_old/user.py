import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field connection be blank"
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help="This field cannot be blank"
    )
#I am going to change this to a classmethod to see if it works
    @classmethod
    def post(cls):
        data = cls.parser.parse_args()

        if UserModel.find_by_username(data['username']) is not None:
            return {"message": "A user with that username already exists"}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {"message": "User created successfully"}, 201
