# 9-3. Users: Make a class called User. Create two attributes called first_name
# and last_name, and then create several other attributes that are typically stored
# in a user profile. Make a method called describe_user() that prints a summary
# of the user’s information. Make another method called greet_user() that prints
# a personalized greeting to the user.
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

# Create several instances representing different users, and call both meth-
# ods for each user.
user_1 = User("Jose","Cantor","josecant@gmail.com","male",25)
user_2 = User("Alexa","Yeehaw","axelayee@gmail.com","female",27)
user_3 = User("Roberto","Hughman","robert@gmail.com","male",60)

user_1.describe_user()
user_2.describe_user()
user_3.describe_user()