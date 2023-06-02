import re
password = input("enter your password: ")
def check_password(password):
    pattern = ".*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])"
    result = re.search(pattern, password)
    if (result):
        print("your password is valid password")
    else:
        print("this is not a valid password")

check_password(password)
#