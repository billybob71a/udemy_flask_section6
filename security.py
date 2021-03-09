from werkzeug.security import safe_str_cmp
from models.user import UserModel


# username_mapping = { 'bob': {
#     'id': 1,
#     'username': 'bob',
#     'password': 'asdf'
#     }
# }

# userid_mapping = { 1: {
#     'id': 1,
#     'username': 'bob',
#     'password': 'asdf'
#     }
# }

def authenticate(username, password):
    user = UserModel.find_by_username(username)
    print("the user is {}".format(username))
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
