class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        
    def display_info(self):
        print("First Name:", self.first_name)
        print("Last Name", self.last_name)
        print("Email", self.email)
        print("Age:", self.age)
        print("Rewards Member", self.is_rewards_member)
        print("Gold card points", self.gold_card_points)
        
    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
        print("Enrollment succesful. Student have 200 gold card points")
        
    def spend_points(self, amount):
       if self.gold_card_points >= amount:
           self.gold_card_points -= amount
           print(amount, "Gold coins spent")
       else:
           print("Insufficient amount")
        
user1 = User("Rob","Love","Roblove@gmail.com","30")
user1.display_info()

user1.enroll()
user1.display_info()

user1.spend_points(100)
user1.display_info()
