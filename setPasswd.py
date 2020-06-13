import passwlib

print("Please enter new Password")
passw = input("Password: ")
print("You entered: [next line]")
print(passw)

passwlib.set_password(passw)

print("Password Successfully Updated!")
