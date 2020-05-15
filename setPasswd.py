import hashlib

print("Please enter new Password")
passw = input("Password: ")
print("You entered: [next line]")
print(passw)

hashpasswd = hashlib.sha256(bytes(passw, encoding="utf-8")).hexdigest()
with open("passw.db", "w") as file:
	file.write(str(hashpasswd))

print("Password Successfully Updated!")
