class User:
    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.password = password
    def login(self):
        print(f"{self.username} logged in successfully.")
        print(f"Email: {self.email}")
        print(f"Password: {self.password}\n")

u1=User("Abdur Rahman","akash.abdur.2002@gmail.com","123456789")
u1.login()

class foreigner_student:
    def __init__(self, name, age, Location, Profession):
        self.name = name
        self.age = age
        self.Location = Location
        self.Profession = Profession
    def login(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Location: {self.Location}")
        print(f"Profession: {self.Profession}")
        # print(f"Name:{self.name}\nAge:{self.age}\nLocation: {self.Location}\nProfession: {self.Profession}")

s1=foreigner_student("Mark", 20, "New York", "Software Engineer")
s1.login()