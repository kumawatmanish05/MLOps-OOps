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
            self.message_friend()
        else:
            exit() 

    def signup(self):
        email = input("Enter your email Here ->")
        pwd = input("Setup your password Here ->")
        self.username = email
        self.password = pwd
        print("You have signed up successfully !!")
        print("\n")
        self.menu()

    def signin(self):
        if self.username == '' and self.password == '':
            print("You need to signup first to signin !!")
        else:
            email = input("Enter your email Here ->")
            pwd = input("Enter your password Here ->")
            if self.username == email and self.password == pwd:
                print("You have signed in successfully !!")
                self.loggedin = True
            else:
                print("Invalid credentials !! Please try again !!")
        print("\n")
        self.menu()
    
    def write_post(self):
        if self.loggedin == True:
            post = input("What's on your mind ?")
            print(f"Your post '{post}' has been posted successfully !!")
        else:
            print("You need to login first to write a post !!")
            print("\n")
            self.menu()

    def message_friend(self):
        if self.loggedin == True:
            friend = input("Enter your friend's name Here ->")
            message = input("Enter your message Here ->")
            print(f"Your message '{message}' has been sent to {friend} successfully !!")
        else:
            print("You need to login first to message a friend !!")
            print("\n")
            self.menu()



# obj = chatbook()
