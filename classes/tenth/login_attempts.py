# 9-5. Login Attempts: Add an attribute called login_attempts to your User 
# class from Exercise 9-3 (page 166) . Write a method called increment_
# login_attempts() that increments the value of login_attempts by 1 . Write 
# another method called reset_login_attempts() that resets the value of login_
# attempts to 0 .
# Make an instance of the User class and call increment_login_attempts() 
# several times . Print the value of login_attempts to make sure it was incremented 
# properly, and then call reset_login_attempts() . Print login_attempts again to 
# make sure it was reset to 0

class User:
    
    def __init__(self, first_name, last_name, email, gender, age, login_attempts = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.email =  email
        self.gender = gender
        self.age = age
        self.login_attempts = login_attempts
    
    def describe_user(self):
        print(f"The user's full name is {(self.first_name+" "+self.last_name).title()}")
        print(f"\t-Email: {self.email}\n\t-Gender: {self.gender}\n\t-Age: {self.age}")

    def get_login_attempts(self):
        return self.login_attempts

    def increment_login_attempts(self, attempts):
        self.login_attempts += attempts

    def reset_login_attempts(self):
        self.login_attempts = 0

# Create several instances representing different users, and call both meth-
# ods for each user.
user_1 = User("Jose","Cantor","josecant@gmail.com","male",25)
user_2 = User("Alexa","Yeehaw","axelayee@gmail.com","female",27)
user_3 = User("Roberto","Hughman","robert@gmail.com","male",60)

user_1.describe_user()
user_2.describe_user()
user_3.describe_user()

print()
user_4 = User("Gary","Manners","imgaary@gmail.com","male",19)
user_4.describe_user()
print(f"{user_4.first_name}'s current logging attempts: {user_4.get_login_attempts()}")
user_4.increment_login_attempts(1)
user_4.increment_login_attempts(2)
user_4.increment_login_attempts(1)
print(f"{user_4.first_name}'s current logging attempts: {user_4.get_login_attempts()}")
user_4.reset_login_attempts()
print(f"{user_4.first_name}'s current logging attempts: {user_4.get_login_attempts()}")