# 7-3. Multiples of Ten: Ask the user for a number, and then report whether the 
# number is a multiple of 10 or not
prompt = "Give me a number\n"

number = input(prompt)

if int(number)%10==0:
    print("The number "+number+" is a multiple of 10")
else:
    print("The number "+number+" is not a multiple of 10")