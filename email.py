name = (input("Enter your name"))
email = (input("enter yor email"))

if len (name) < 2 :
    print("the length must be greater than 2")
elif " " in email:
    print("the email should not contain spaces, please provid a valid email")
elif email.count("@") != 1:
    print("The email format is invalid, please provide one '@' only.")  
elif not (email.endswith("@gmail.com")):
    print("The email is not valid, please provide a valid Gmail address.")
else:
     print(f"Welcome {name}, you registered with the email{email}!")