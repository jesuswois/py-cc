# 10-5. Programming Poll: Write a while loop that asks people why they like
# programming. Each time someone enters a reason, add their reason to a file
# that stores all the responses.

file_path = "poll_responses.txt"

with open(file_path,'w') as file_object:
    print("\n\tProgramming Poll! All participants must enter a reason to why they like programming.")
    print("NOTE: To end the poll just enter 0!\n")

    while True:
        input_reason = input("Enter your reason: ")
        if input_reason == '0':
            print("Exiting...")
            break
        file_object.write(f"{input_reason}\n")
