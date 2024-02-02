from controller.user_controller import UserController
from model.da.user_da import UserDa
from model.entity.user import User

### TEST DATA ACCESS
# user_da = UserDa()

# user = User("ali", "ali123", "1001")
# user_da.save(user)

# user = User("ali", "ali456")
# user.id = 2
# user_da.edit(user)

# print(user_da.find_by_id("2"))
# print(user_da.find_by_username("ali"))
# print(user_da.find_by_username_and_password("ali", "ali456"))

# print(user_da.find_by_id("3"))
# print(user_da.find_by_username("reza"))
# print(user_da.find_by_username_and_password("ali", "ali444"))


### TEST CONTROLLER
controller = UserController()
print(controller.save("rezaa", "reza123", "username", "password", "customer"))

# print(controller.edit(4, "bbb", "cccc"))

# print(controller.find_by_id(2))

# print(controller.find_by_username("ali111"))
# print(controller.find_by_username_and_password("ali", "ali456111"))