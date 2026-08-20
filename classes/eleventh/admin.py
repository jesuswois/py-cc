# 9-7. Admin: An administrator is a special kind of user . Write a class called 
# Admin that inherits from the User class you wrote in Exercise 9-3 (page 166) 
# or Exercise 9-5 (page 171) . Add an attribute, privileges, that stores a list 
# of strings like "can add post", "can delete post", "can ban user", and so on . 
# Write a method called show_privileges() that lists the administrator’s set of 
# privileges . Create an instance of Admin, and call your method .

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

class Admin(User):

    def __init__(self, first_name, last_name, email, gender, age, privileges = []):
        super(Admin, self).__init__(first_name, last_name, email, gender, age)
        self.privileges = privileges

    def show_privileges(self):
        print(f"The Admin's privileges are:")
        for privilege in self.privileges:
            print(f"\t-{privilege.title()}")

admin = Admin("Koorb","Nerva","k00rb@gmail.com",
              "Male",21,["can add posts","can ban users","can update posts","can delete posts"])
admin.show_privileges()