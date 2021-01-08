import getpass
def sign_in(username_for_user, password_of_user):
  username = input("Enter your username: ")
  if username != username_for_user:
    print ("Wrong username")
    return "Wrong Username, Try again"
  else:
    return "Correct Username"
    password = getpass.getpass("Enter the password for this username: ")
    if password != password_of_user:
      print("Wrong Password")
      return "Wrong Password, Try again"
    else:
     return "Correct Password"
  if user == username and passw == password:
    return "1"
    print("Successful Sign In")
