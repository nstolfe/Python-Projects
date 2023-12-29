#Game idea: Dino Duel: T-rex vs Stegosaurus using cowsay.
#Trex: High Attack, low defense, medium health, medium speed
#Stegosarus: Low attack, high defense, high health, low speed

#Known Problems: 

#Create at least two classes:
  #1.)Dinosaur
  #2.)Player
#__init__ all classes
#Each class needs three attributes: ex: self.name, self.age, self.color:
  #Dinosaur: #1) Attack, #2) Defense, #3) Health
  #Player: #1) Active Dinosaur #2) Defeated Dinosaur #3) Dinosaur Name
#Each class needs three methods: ex: def change_color(self, color):
  #Dinosaur: attack, lose health, heal
  #Player: Name Dinosaur, Revive dinosaur, check active dinosars? check defeated dinosaurs?
#Each class needs to describe itself with __repr__(self):
#Each class needs to have at least two instances (or class objects)
  #Dinosaur Class instances: T-rex and Stegosarus
  #Player Class instances: Player 1 and Player 2
#The two classes need to interact with each other in some way
  #Revive dinosaur
#Additonal Ideas:
  #Use a while loop to check dinosaur hp and keep rotating between players to take actions?

import cowsay

class Dinosaur:
    def __init__(self, attack, defense, health, species = "t-rex"):
        self.attack = attack
        self.defense = defense
        self.health = health
        self.species = species

    #Calculates and updates remaining health of the dinosaur
    def lose_health(self, damage_dealt):
        self.health -= damage_dealt
        if self.species == "t-rex":
            print("After the attack, the T-rex has {health} hit points remaining.".format(health = self.health))
        else:
            print("After the attack, the Stegosarus has {health} hit points remaining.".format(health = self.health))
        return self.health

    #Calculates hit point loss for the update_health function
    def deal_damage(self):
        if self.species == "t-rex":
            damage_dealt = 40
        else:
            damage_dealt = 20
        #Allows the damage calculated to be passed into the parameter for damage_dealt in the update_health function
        return damage_dealt
    
    #Allows a non-defeated dinosaur to heal by 100HP
    def heal_self(self):
        if self.species == "t-rex":
            if self.health > 0:
                self.health += 100
                print("Your T-rex steps away from the duel to rest for a moment. Your T-rex heals by 100 HP and now has {health}HP.".format(health = self.health))
            else:
                print("Your T-rex is already defeated in battle.")
        else:
            if self.health > 0:
                self.health += 100
                print("Your Stegosarus steps away from the duel to rest for a moment. Your Stegosarus heals by 100 HP and now has {health}HP.".format(health = self.health))
            else:
                print("Your Stegosarus is already defeated in battle.")

    def __repr__(self):
        return """Your dinosaur is a {species}.\nYour {species} has {health} hit points, {attack} attack power, {defense} defense power.""".format(species = self.species.title(), health = self.health, attack = self.attack, defense = self.defense)

 
class Player:
    def __init__(self, active_dinosaurs, defeated_dinosaurs, player = "Player 1"):
        self.active_dinosaurs = active_dinosaurs
        self.defeated_dinosaurs = defeated_dinosaurs

    def name_dinosaur(self):
        pass

    def check_active_dinosaurs(self, active_dinosaurs):
        # for dinosaur in active_dinosaurs:
        #     print(dinosaur)

        #use "is defeated == true" identifier?
        print("Your active dinosaurs are {dinosaur}".format(dinosaur = self.active_dinosaurs))
    
    def revive_dinosaur(self):
        pass

#Creating the dinosaurs that will duel
trex1 = Dinosaur(100, 20, 600, "t-rex")
stegosaurus1 = Dinosaur(40, 60, 1000, "stegosarus")
trex2 = Dinosaur(150, 70, 650, "t-rex")
stegosaurus2 = Dinosaur(90, 110, 1050, "stegosarus")

#Creating player list of active dinosaurs
player_one_dino_list = [trex1, trex2]
player_two_dino_list = [stegosaurus1, stegosaurus2]

#Creating player list of inactive, defeated dinosaurs
player_one_defeated_dinos = []
player_two_defeated_dinos = []

#Creating the two players
player_one = Player(player_one_dino_list, player_one_defeated_dinos, "Player 1")
player_two = Player(player_two_dino_list, player_two_defeated_dinos, "Player 2")

#The start of what will display in the terminal

user_trex1_name = input("Welcome to Dino Duel, Player 1. Player 1 you are the two T-rexes. Player 1, what would you like the name of your first t-rex to be? ")
user_stego1_name = input("Welcome to Dino Duel, Player 2. Player 2 you are the Stegosaruses. Player 2, what would you like the name of your first stegosaurus to be? ")
#Accounting for any user capitalization errors to the dinosaur name
trex1_name = user_trex1_name.title()
stego1_name = user_stego1_name.title()

user_trex2_name = input("Player 1, what would you like the name of your second t-rex to be? ")
user_stego2_name = input("Player 2, what would you like the name of your second stegosaurus to be? ")
#Accounting for any user capitalization errors to the dinosaur name
trex2_name = user_trex2_name.title()
stego2_name = user_stego2_name.title()

#Returning the names of the dinosaurs to the terminal with the dinosaur text art
print(cowsay.trex("The first T-rex is named " + trex1_name))
print(cowsay.stegosaurus("The first Stegosarus is named " + stego1_name))
print(cowsay.trex("The second T-rex is named " + trex2_name))
print(cowsay.stegosaurus("The second Stegosarus is named " + stego2_name))

#player_one.check_active_dinosaurs(player_one_dino_list)

stegosaurus1.lose_health(trex1.deal_damage())
stegosaurus1.lose_health(trex1.deal_damage())
stegosaurus1.lose_health(trex1.deal_damage())

trex1.lose_health(stegosaurus1.deal_damage())
trex1.lose_health(stegosaurus1.deal_damage())
trex1.lose_health(stegosaurus1.deal_damage())

trex1.heal_self()
stegosaurus1.heal_self()

print(trex1)
print(stegosaurus1)