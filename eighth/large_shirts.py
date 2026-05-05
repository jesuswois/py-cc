# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large 
# by default with a message that reads I love Python . Make a large shirt and a 
# medium shirt with the default message, and a shirt of any size with a different 
# message.
def make_shirt(size="large", text="I love Python"):
    print("Making a shirt with the attributes...")
    print("\tSize: "+size+"\n\tText: "+text)

make_shirt("small","HELL NAW")
make_shirt(text="BRUH",size="medium")
make_shirt(size="medium")
make_shirt(text="HECK YEAH")