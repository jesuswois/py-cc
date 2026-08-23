# 9-12. Multiple Modules: Store the User class in one module, and store the
# Privileges and Admin classes in a separate module. In a separate file, create
# an Admin instance and call show_privileges() to show that everything is still
# working correctly.

from multiple_modules_classes_02 import Admin

my_admin = Admin("Curen","Odd","theeodd@gmail.com","male",5,["can melt people on sight"])

my_admin.describe_user()