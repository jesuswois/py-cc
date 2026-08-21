""" Class used to represent user """
from multiple_modules_classes_01 import User
class Privileges:
    def __init__(self, privileges = []):
        self.privileges = privileges

    def show_privileges(self):
        print(f"The Admin's privileges are:")
        for privilege in self.privileges:
            print(f"\t-{privilege.title()}")

class Admin(User):

    def __init__(self, first_name, last_name, email, gender, age, privileges = []):
        super(Admin, self).__init__(first_name, last_name, email, gender, age)
        self.privileges = Privileges(privileges)

    def show_privileges(self):
        print(f"The Admin's privileges are:")
        for privilege in self.privileges:
            print(f"\t-{privilege.title()}")
