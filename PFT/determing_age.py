
def number(message):
  while True:
    try:
       years = int(input("What is your age?:  ")       
    except ValueError:
       print("You entered an invalid input. Please try again.")
       continue
    else:
       return years 
       break 


#Recieve users age
def age(years):
    while True:
        if years < 17:
            print("You are too young to serve")
            break
        elif years >= 17:
            print("You are %")
            break
        else:
            print("You entered an invalid input. Please try again.")
        

age(years)
