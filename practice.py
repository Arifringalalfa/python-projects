class user:
    name = ""
    password = ""
    email = ""
    Login = True


    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def login(self):
        email = input("Enter your email here: ")
        password = input("Enter your password here: ")
        if email == self.email and password == self.password:
            login = True
            print("Login successfully")

        else:
            print("Login Failed")        

    def logout(self):
        login = False
        print("LOgged Out")

    def IsLoggedIn(self):
        if self.login:
            return True
        else:
            return False
    
    def profile(self):
        if self.IsLoggedIn:
            print(self.name, "\n", self.email)

        else:
            print("User is not in online")

user1 = user("arif", "arif@gmail.com", "12345")


user1.login()
user1.profile()