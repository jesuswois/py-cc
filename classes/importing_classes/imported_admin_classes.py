""" Class used to represent all possible roles & their methods/attributes """
class User:
    
    def __init__(self, first_name, last_name, email, gender, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email =  email
        self.gender = gender
        self.age = age
    
    def describe_user(self):
        print(f"The user's full name is {(self.first_name+" "+self.last_name).title()}")
        print(f"\t-Email: {self.email}\n\t-Gender: {self.gender}\n\t-Age: {self.age}")

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
