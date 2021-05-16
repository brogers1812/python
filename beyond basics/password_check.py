correct_password = "python123"
name = input("Enter name: ")
surname = input("Enter surname: ")
password = input("Enter Password: ") 

while correct_password != password:
    password = input("Wrong password! Enter again: ")

print("Hi", name, "You are Logged In")
print("Hi %s %s, you are logged in " % (name,surname))