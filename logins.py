import re
from wordsegment import load, segment
def main():
    login()

"""
this module simply ensures the user enters a valid email address and password
of user's input is considered unconventional, user is printed a hint "Invalid entry"
and prompted to enter their details again
if user enters conventional email address and password, it is validated as valid and the loop is broken from
"""
def login():
    while True:
        email = input("What's your email: ").strip()
        password = input("What's is your password: ")

        if re.fullmatch(r"\w+(\.\w+)*@(\w+\.)*\w+\.(com|edu|gov|net|org)", email, re.IGNORECASE) and re.match(r"\w+(\W)*", password):
            print()
            print("LOGIN SUCCESSFUL")
            break
        
        print("INVALID CREDENTIALS! please try again")

    print("You are now connected to the server")
    print()
    """
    this module below searches throught the user's input(email) and then extracts the username
    proceeds to strip off trailing numeric characters and then segments the username to first and last name
    proceeds to print a message "hello, dr first name"
    """
    load()
    #search over the email address and capture the username of the user
    if match := re.search(r"^(\w+)@(\w+\.)?\w+\.(com|edu|gov|net|org)$", email):
        #assign to the username variable the return value of group(1) match.
        #match.group(1) simply means a capture of the parentheses to the right of the "@" sign 
        username = match.group(1)
        #strip off any numeric character from username to ensure proper segmentation
        stripped_username = re.sub(r'\d+', "", username)
        #assign the return value of the segment function to name_parts
        #segment() returns a list of values
        name_parts = segment(stripped_username)
        #index into name_parts and access the first item in the list
        print(f"Welcome, Dr {name_parts[0].title()}.")
    print()

if __name__ == "__main__":
    main()