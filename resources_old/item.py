from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="This field definitely cannot be left blank"
                        )
    parser.add_argument('store_id',
                        type=int,
                        required=True,
                        help="Every item needs a store id"
                        )

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404

        if row:
            return{'item':{'name':row[0],'price': row[1]}}
        return {'message': 'Item not found'}, 404

    def post(self, name):
        print("the name is {}".format(name))

        if ItemModel.find_by_name(name):
            return {'message': "An item with name '{}' already exists.".format(name)}, 400
        data = Item.parser.parse_args()
        print("the keys are {}".format(data.keys))
        print("the data is here")

        item = ItemModel(name, **data)
        print("I am inserting and item")
        try:
            item.save_to_db()
        except Exception as e:
            print(e)
            return {"message": "An really bad error occurred inserting the item."}, 500
        return item.json(), 201

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()

        return {'message': 'Item deleted'}

    def put(self, name):
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)

        if item is None:
            item = ItemModel(name, **data)
        else:
            item.price = data['price']

        item.save_to_db()

        return item.json()


class ItemList(Resource):
    def get(self):

        return {"items": [item.json() for item in ItemModel.query.all()]}
