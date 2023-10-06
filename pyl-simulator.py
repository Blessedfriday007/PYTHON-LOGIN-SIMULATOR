# Python login simulator

# a dictionary used to store registered users.

userA = {}

# A function to display the menu and ask for the users choice of action...
def action():
 
 print("Welcome to the python simulator program...")
print("Welcome to the python simulator program...\n")
print("Please choose an option\n")
print("(a) Login\n")
print("(b) Register\n")
print("(c) Exit\n")
choose = input("Make your choice: ")

# function to validate users login details

def login():
 username = input("Enter your username: ")
 passkey = input ("Enter your password:")
 if username in userA and userA[username] == passkey:
  print("Invalid username or password:\n")
 else:
  print("Login Successful...\n")


#A function to register new members...

def registration():
 username = input ("Register a username: ")
 if username in userA:
  print("This username is not available, or already taken!...")
 else:
  passkey = input ("Enter a password!... ")
  userA[username] = passkey 
  print("Congratulations, Registration successful!...\n ")
  return login()

  #Loop

if choose == "a":
        login()
elif choose == "b":
        registration()
elif choose == "c":
        print("Thank you for using the python simulator program Goodbye!")
        
        
else:
        print("Invalid input, Please select a, b, or c")
 
       
      







