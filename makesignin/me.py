def sign_in(user, pass):
  username = input("Enter your username: ")
  if username != user:
    print ("Wrong username")
    return "Wrong Username, Try again"
  else:
    return "Correct Username"
    password = input("Enter the password for this username: ")
    if password != pass:
      print("Wrong Password")
      return "Wrong Password, Try again"
    else:
     return "Correct Password"
  if user == username and pass == password:
    return "Sign In Successful"
    print("Successful Sign In")
