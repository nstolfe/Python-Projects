#Project Requirements:

#Create at least two classes: DONE
  #1.)Dinosaur
  #2.)Player

#__init__ all classes DONE

#Each class needs three attributes: ex: self.name, self.age, self.color:
  #Dinosaur: #1) Attack, #2) Defense, #3) Health DONE
  #Player: #1) Active Dinosaur #2) Defeated Dinosaur #3) Revival Tokens

#Each class needs three methods: ex: def change_color(self, color):
  #Dinosaur: deal damage (attack), lose health, heal DONE
  #Player: Revive dinosaur, check active dinosars, check defeated dinosaurs

#Each class needs to describe itself with __repr__(self):

#Each class needs to have at least two instances (or class objects) DONE
  #Dinosaur Class instances: T-rex and Stegosarus
  #Player Class instances: Player 1 and Player 2

#The two classes need to interact with each other in some way DONE
  #Check active/defeated dinosaur

#Left to do:
    #Create final player method
    #Describe player class with __repr__

#Allows the text art of the dinosaurs that will be shown in the terminal when players name the dinosaurs.
    #Uses cowsay.trex() and cowsay.stegosaurus() to designate the T-rex and Stegosaurs art.
import cowsay

class Dinosaur:
    def __init__(self, attack, defense, health, name, species):
        self.attack = attack
        self.defense = defense
        self.health = health
        self.name = name
        self.species = species

    #Calculates and updates remaining health of the dinosaur.
    def lose_health(self, damage_dealt):
        self.health -= damage_dealt
        if self.species == "t-rex":
            print("After the attack, the T-rex has {health} hit points remaining.".format(health = self.health))
        else:
            print("After the attack, the Stegosarus has {health} hit points remaining.".format(health = self.health))

    #Calculates hit point loss for the update_health function.
    def deal_damage(self):
        if self.species == "t-rex":
            damage_dealt = 40
        else:
            damage_dealt = 20
        #Allows the damage calculated to be passed into the parameter for damage_dealt in the update_health function
        return damage_dealt
    
    #Allows a non-defeated dinosaur to heal by 100HP.
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

    #Allows player to check the stats of their dinosaur.
    def __repr__(self):
        return """Your dinosaur is a {species}.\nYour {species} has {health} hit points, {attack} attack power, {defense} defense power.""".format(species = self.species.title(), health = self.health, attack = self.attack, defense = self.defense)

class Player(Dinosaur):
    def __init__(self, active_dinosaurs, defeated_dinosaurs, revival_tokens):
        self.active_dinosaurs = active_dinosaurs
        self.defeated_dinosaurs = defeated_dinosaurs
        self.revival_tokens = revival_tokens

    #Allows the player to see which dinosaurs are still active in battle. Dinosaurs will be referenced by the name the player provided earlier.
    def check_active_dinosaurs(self, active_dinosaurs, defeated_dinosaurs):
        #Checking if the dinosaur has health left to be considered active or not. This will move dinosaurs from the active dinosaur list
        #to the defeated dinosaur list if the dinosaur is defeated in battle.
        for Dinosaur in active_dinosaurs:
            if Dinosaur.health <= 0:
                defeated_dinosaurs.append(Dinosaur)
                active_dinosaurs.remove(Dinosaur)
        #This allows a dinosaur to be moved from the defeated dinosaur list to the active dinosaur list if the dinosaur is revived
        #from the revive_dinosaur function and allows the check_active_dinosaurs function to be called without giving an
        #unbound local variable error in some cases before the check_defeated_dinosaurs function is called.
        for Dinosaur in defeated_dinosaurs:
            if Dinosaur.health > 0:
                defeated_dinosaurs.remove(Dinosaur)
                active_dinosaurs.append(Dinosaur)

        #Using the active dinosaur list defined when the player object is later created to determine which dinosaur name should be
        #returned when the active dinosaur list is called.
        if len(active_dinosaurs) == 1:
            for Dinosaur in active_dinosaurs:
                if Dinosaur.species == "t-rex":
                    if Dinosaur.name == trex_name:
                        print("Your active dinosaur is {dinosaur}.".format(dinosaur = trex_name))
                    elif Dinosaur.name == trex2_name:
                        print("Your active dinosaur is {dinosaur}.".format(dinosaur = trex2_name))
                else:
                    for Dinosaur in active_dinosaurs:
                        if Dinosaur.name == stego_name:
                            print("Your active dinosaur is {dinosaur}.".format(dinosaur = stego_name))
                        if Dinosaur.name == stego2_name:
                            print("Your active dinosaur is {dinosaur}.".format(dinosaur = stego2_name))
        if len(active_dinosaurs) == 2:
            if Dinosaur.species == "t-rex":
                print("Your active dinosaurs are {dinosaur1} and {dinosaur2}.".format(dinosaur1 = trex_name, dinosaur2 = trex2_name))
            else:
                print("Your active dinosaurs are {dinosaur1} and {dinosaur2}.".format(dinosaur1 = stego_name, dinosaur2 = stego2_name))
        elif len(active_dinosaurs) == 0:
            print("You have no active dinosaurs to duel with.")
            
    #Allows the player to see which dinosaurs are still active in battle. Dinosaurs will be referenced by the name the player provided earlier.
    def check_defeated_dinosaurs(self, defeated_dinosaurs, active_dinosaurs):
        #Checking if the dinosaur has health left to be considered defeated or not. This allows the defeated dinosaur function to be called
        #without relying on the check_active_dinosaurs function to be called first. These loops prevent an unbound local variable error when
        #the function is called without the check_active_dinosaurs function being called first in the case where a dinosaur is defeated but 
        #has not yet been moved from the active_dinosaur list.
        for Dinosaur in active_dinosaurs:
            if Dinosaur.health <= 0:
                defeated_dinosaurs.append(Dinosaur)
                active_dinosaurs.remove(Dinosaur)

        #Checking if a defeated dinosaur has been revived when the revive_dinosaur function is called and removing it from the list if
        #the dinosaur has been revived.
        for Dinosaur in defeated_dinosaurs:
            if Dinosaur.health > 0:
                defeated_dinosaurs.remove(Dinosaur)
                active_dinosaurs.append(Dinosaur)
        
        #Using the defeated_dinos list defined when the player object is created to determine which dinosaur should be
        #printed when the defeated_dinos list is called.
        if len(defeated_dinosaurs) == 1:
            for Dinosaur in defeated_dinosaurs:
                if Dinosaur.species == "t-rex":
                    if Dinosaur.name == trex_name:
                        print("Your defeated dinosaur is {dinosaur}.".format(dinosaur = trex_name))
                    elif Dinosaur.name == trex2_name:
                        print("Your defeated dinosaur is {dinosaur}.".format(dinosaur = trex2_name))
                else:
                    for Dinosaur in defeated_dinosaurs:
                        if Dinosaur.name == stego_name:
                            print("Your defeated dinosaur is {dinosaur}.".format(dinosaur = stego_name))
                        if Dinosaur.name == stego2_name:
                            print("Your defeated dinosaur is {dinosaur}.".format(dinosaur = stego2_name))
        if len(defeated_dinosaurs) == 2:
            if Dinosaur.species == "t-rex":
                print("Your defeated dinosaurs are {dinosaur1} and {dinosaur2}. You currently have no active dinosaurs to duel with.".format(dinosaur1 = trex_name, dinosaur2 = trex2_name))
            else:
                print("Your defeated dinosaurs are {dinosaur1} and {dinosaur2}. You currently have no active dinosaurs to duel with.".format(dinosaur1 = stego_name, dinosaur2 = stego2_name))
        elif len(defeated_dinosaurs) == 0:
            print("You have no defeated dinosaurs.")

    def revive_dinosaur(self):
        pass

    def __repr__(self):
        return super().__repr__()

#The start of what will display in the terminal.

#Global variables that will contain the names of the dinosaurs designated by the player.
trex_name = input("Welcome to Dino Duel, Player 1. Player 1 you are the two T-rexes. Player 1, what would you like the name of your first t-rex to be? ").title()
trex2_name = input("Player 1, what would you like the name of your second t-rex to be? ").title()
stego_name = input("Welcome to Dino Duel, Player 2. Player 2 you are the Stegosaruses. Player 2, what would you like the name of your first stegosaurus to be? ").title()
stego2_name = input("Player 2, what would you like the name of your second stegosaurus to be? ").title()

#Creating the dinosaur objects that will duel.
trex1 = Dinosaur(100, 20, 600, trex_name, "t-rex")
stegosaurus1 = Dinosaur(40, 60, 1000, stego_name, "stegosarus")
trex2 = Dinosaur(150, 70, 650, trex2_name, "t-rex")
stegosaurus2 = Dinosaur(90, 110, 1050, stego2_name, "stegosarus")

#Creating player list of active dinosaurs.
player_one_dino_list = [trex1, trex2]
player_two_dino_list = [stegosaurus1, stegosaurus2]

#Creating player list of inactive, defeated dinosaurs.
player_one_defeated_dinos = []
player_two_defeated_dinos = []

#Creating the two player objects.
player_one = Player(player_one_dino_list, player_one_defeated_dinos, 1)
player_two = Player(player_two_dino_list, player_two_defeated_dinos, 1)

print(cowsay.trex("The first T-rex is named " + trex_name))
print(cowsay.trex("The second T-rex is named " + trex2_name))
print(cowsay.stegosaurus("The first Stegosarus is named " + stego_name))
print(cowsay.stegosaurus("The second Stegosarus is named " + stego2_name))

#Simulating a battle below:

#testing checking dinosaur stats before duel begins
print(trex1)
print(stegosaurus1)
print(trex2)
print(stegosaurus2)

#testing active dinosaur function with all dinosaurs active
player_one.check_active_dinosaurs(player_one_dino_list, player_one_defeated_dinos)
player_two.check_active_dinosaurs(player_two_dino_list, player_two_defeated_dinos)

#testing defeated dinosaur function with no dinosaurs defeated
player_one.check_defeated_dinosaurs(player_one_defeated_dinos, player_one_dino_list)
player_two.check_defeated_dinosaurs(player_two_defeated_dinos, player_two_dino_list)

#testing deal damage and lose health functions
trex2.lose_health(stegosaurus1.deal_damage())
trex1.lose_health(stegosaurus2.deal_damage())

stegosaurus1.lose_health(trex1.deal_damage())
stegosaurus2.lose_health(trex2.deal_damage())

#testing heal self function
trex1.heal_self()
trex2.heal_self()

stegosaurus1.heal_self()
stegosaurus2.heal_self()

#Defeating a dinosaur to test active and defeated list when a dinosaur is defeated
trex1.lose_health(stegosaurus2.deal_damage())
trex1.lose_health(stegosaurus2.deal_damage())
trex1.lose_health(stegosaurus2.deal_damage())
trex1.lose_health(stegosaurus2.deal_damage())
trex1.lose_health(stegosaurus2.deal_damage())
trex1.lose_health(stegosaurus2.deal_damage())
trex1.lose_health(stegosaurus2.deal_damage())
trex1.lose_health(stegosaurus2.deal_damage())
trex1.lose_health(stegosaurus2.deal_damage())
trex1.lose_health(stegosaurus2.deal_damage())
trex1.lose_health(stegosaurus2.deal_damage())
trex1.lose_health(stegosaurus2.deal_damage())
trex1.lose_health(stegosaurus2.deal_damage())
trex1.lose_health(stegosaurus2.deal_damage())
trex1.lose_health(stegosaurus2.deal_damage())
trex1.lose_health(stegosaurus2.deal_damage())
trex1.lose_health(stegosaurus2.deal_damage())
trex1.lose_health(stegosaurus2.deal_damage())
trex1.lose_health(stegosaurus2.deal_damage())
trex1.lose_health(stegosaurus2.deal_damage())
trex1.lose_health(stegosaurus2.deal_damage())
trex1.lose_health(stegosaurus2.deal_damage())
trex1.lose_health(stegosaurus2.deal_damage())
trex1.lose_health(stegosaurus2.deal_damage())
trex1.lose_health(stegosaurus2.deal_damage())
trex1.lose_health(stegosaurus2.deal_damage())
trex1.lose_health(stegosaurus2.deal_damage())
trex1.lose_health(stegosaurus2.deal_damage())
trex1.lose_health(stegosaurus2.deal_damage())
trex1.lose_health(stegosaurus2.deal_damage())
trex1.lose_health(stegosaurus2.deal_damage())
trex1.lose_health(stegosaurus2.deal_damage())
trex1.lose_health(stegosaurus2.deal_damage())
trex1.lose_health(stegosaurus2.deal_damage())

#testing check active dinosaurs after a dinosaur is defeated
player_one.check_active_dinosaurs(player_one_dino_list, player_one_defeated_dinos)

#testing check defeated dinosaurs after a dinosaur is defeated
player_one.check_defeated_dinosaurs(player_one_defeated_dinos, player_one_dino_list)

#defeating a dinosaur from player two:
stegosaurus2.lose_health(trex2.deal_damage())
stegosaurus2.lose_health(trex2.deal_damage())
stegosaurus2.lose_health(trex2.deal_damage())
stegosaurus2.lose_health(trex2.deal_damage())
stegosaurus2.lose_health(trex2.deal_damage())
stegosaurus2.lose_health(trex2.deal_damage())
stegosaurus2.lose_health(trex2.deal_damage())
stegosaurus2.lose_health(trex2.deal_damage())
stegosaurus2.lose_health(trex2.deal_damage())
stegosaurus2.lose_health(trex2.deal_damage())
stegosaurus2.lose_health(trex2.deal_damage())
stegosaurus2.lose_health(trex2.deal_damage())
stegosaurus2.lose_health(trex2.deal_damage())
stegosaurus2.lose_health(trex2.deal_damage())
stegosaurus2.lose_health(trex2.deal_damage())
stegosaurus2.lose_health(trex2.deal_damage())
stegosaurus2.lose_health(trex2.deal_damage())
stegosaurus2.lose_health(trex2.deal_damage())
stegosaurus2.lose_health(trex2.deal_damage())
stegosaurus2.lose_health(trex2.deal_damage())
stegosaurus2.lose_health(trex2.deal_damage())
stegosaurus2.lose_health(trex2.deal_damage())
stegosaurus2.lose_health(trex2.deal_damage())
stegosaurus2.lose_health(trex2.deal_damage())
stegosaurus2.lose_health(trex2.deal_damage())
stegosaurus2.lose_health(trex2.deal_damage())
stegosaurus2.lose_health(trex2.deal_damage())
stegosaurus2.lose_health(trex2.deal_damage())

#testing checking defeated dinosaurs before checking the active list
player_two.check_defeated_dinosaurs(player_two_defeated_dinos, player_two_dino_list)
player_two.check_active_dinosaurs(player_two_dino_list, player_two_defeated_dinos)

#defeating all dinosuars for a player to test the check active and defeated dinosaurs after no active dinosaurs remain
stegosaurus1.lose_health(trex1.deal_damage())
stegosaurus1.lose_health(trex1.deal_damage())
stegosaurus1.lose_health(trex1.deal_damage())
stegosaurus1.lose_health(trex1.deal_damage())
stegosaurus1.lose_health(trex1.deal_damage())
stegosaurus1.lose_health(trex1.deal_damage())
stegosaurus1.lose_health(trex1.deal_damage())
stegosaurus1.lose_health(trex1.deal_damage())
stegosaurus1.lose_health(trex1.deal_damage())
stegosaurus1.lose_health(trex1.deal_damage())
stegosaurus1.lose_health(trex1.deal_damage())
stegosaurus1.lose_health(trex1.deal_damage())
stegosaurus1.lose_health(trex1.deal_damage())
stegosaurus1.lose_health(trex1.deal_damage())
stegosaurus1.lose_health(trex1.deal_damage())
stegosaurus1.lose_health(trex1.deal_damage())
stegosaurus1.lose_health(trex1.deal_damage())
stegosaurus1.lose_health(trex1.deal_damage())
stegosaurus1.lose_health(trex1.deal_damage())
stegosaurus1.lose_health(trex1.deal_damage())
stegosaurus1.lose_health(trex1.deal_damage())
stegosaurus1.lose_health(trex1.deal_damage())
stegosaurus1.lose_health(trex1.deal_damage())
stegosaurus1.lose_health(trex1.deal_damage())
stegosaurus1.lose_health(trex1.deal_damage())
stegosaurus1.lose_health(trex1.deal_damage())
stegosaurus1.lose_health(trex1.deal_damage())

player_two.check_active_dinosaurs(player_two_dino_list, player_two_defeated_dinos)
player_two.check_defeated_dinosaurs(player_two_defeated_dinos, player_two_dino_list)

#testing heal self function afte a dinosaur is defeated
stegosaurus1.heal_self()

#testing checking dinosaur stats after duel is over
print(trex1)
print(stegosaurus1)
print(trex2)
print(stegosaurus2)