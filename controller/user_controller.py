from model.entity.user import User
from model.da.user_da import UserDa


class UserController:
    @classmethod
    def save(cls,  name, family, username, password, role, status=True):
        try:
            user = User(name, family, username,password, role,status)
            da = UserDa()
            return da.save(user)
        except Exception as e:
            return e
    def edit(self,  id, name, family, username, password, role, status):
        pass


    def remove(self, id):
        pass


    def find_all(self):

        try:
            da = UserDa()
            return da.find_all()
        except Exception as e:
            return e

    def find_by_id(self, id):
        pass


    def find_by_username(self, username):
        pass


    def find_by_username_and_password(self, username, password):
        pass