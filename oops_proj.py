class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()


    def menu(self):
        user_input = input("""Welcome to Chatbook How would you like to procedd?
                            1.Press 1 to signup
                            2.Press 2 to signin
                            3.Press 3 to write a post
                            4.Press 4 to message a friend
                            5.Press any other Key to exit""")
        
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.write_post()
        elif user_input == "4":
            pass
        else:
            exit() 

    def signup(self):
        email = input("Enter your email Here ->")
        pwd = input("Setup your password Here ->")
        self.username = email
        self.password = pwd
        print("You have signed up successfully !!")
        self.menu()

    def signin(self):
        email = input("Enter your email Here ->")
        pwd = input("Enter your password Here ->")
        if self.username == email and self.password == pwd:
            print("You have logged in successfully !!")
            self.loggedin = True
        else:
            print("Invalid credentials, Please try again !!")
            self.menu()
    
    def write_post(self):
        if self.loggedin:
            post = input("What's on your mind ?")
            print(f"Your post '{post}' has been posted successfully !!")
        else:
            print("You need to login first to write a post !!")
            self.menu()



obj = chatbook()
