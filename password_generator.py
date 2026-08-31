import secrets
import string
print("Password Generator")
print("-----------------------------")
length = int(input("Enter password length: "))
characters = string.ascii_letters + string.digits + string.punctuataion
password = ''.join(secrets.choice(characters) for _ in 
range(length))
print("\nGenerated Password:")
print(password)
