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
    
    def __init__(self, first_name, last_name, email, gender, age):
        self.first_name = first_name;
        self.last_name = last_name;
        self.email =  email;
        self.gender = gender;
        self.age = age;
        self.loggin_attempts = 0;
    
    def describe_user(self):
        print(f"The user's full name is {(self.first_name+" "+self.last_name).title()}");
        print(f"\t-Email: {self.email}\n\t-Gender: {self.gender}\n\t-Age: {self.age}\
              \n\tLogging Attempts: {self.loggin_attempts}");

    def increment_login_attempts(self):
        self.loggin_attempts += 1;

    def reset_login_attempts(self):
        self.loggin_attempts = 0;

user_1 = User("jesús","domínguez ramírez","hombre@gmail.com","hombre",21)
user_1.increment_login_attempts()
user_1.describe_user()
user_1.reset_login_attempts()
user_1.describe_user()