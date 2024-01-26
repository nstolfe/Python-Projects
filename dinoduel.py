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

    #Calculates and updates remaining health of the dinosaur by subtracting the damage dealt from the deal_damage function.
    def lose_health(self, damage_dealt):
        self.health -= damage_dealt
        if self.species == "t-rex":
            print("After the attack, the T-rex has {health} hit points remaining.".format(health = self.health))
        else:
            print("After the attack, the Stegosarus has {health} hit points remaining.".format(health = self.health))

    #Calculates hit point loss for the update_health function based on the dinosaur that is attacking and the dinosaur that is defending.
    #This number will be passed into the lose_health function above to update the health of a dinosaur based on how much damage was dealt.
    def deal_damage(self, Dinosaur):
        damage_dealt = self.attack - Dinosaur.defense
        #Allows the damage calculated to be passed into the parameter for damage_dealt in the update_health function
        return damage_dealt
    
    #Allows a non-defeated dinosaur to heal by 100HP and update the remaining health.
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
    
    #This function will revive a dinosaur only if it has been defeated in battle and if a player has a revival token left.
    #This function will inform a player if they are trying to revive a non-defeated dinosaur or if they're trying to revive a dinosaur
    #without having any revival tokens left to use.
    def revive_dinosaur(self, Dinosaur):
        if self.revival_tokens == 1:
            if Dinosaur.health <= 0:
                Dinosaur.health += 300
                self.revival_tokens -= 1
                print("Your dinosaur was revived and now has {health} hit points remaining.".format(health = Dinosaur.health))
            elif Dinosaur.health > 0:
                print("You cannot revive a dinosaur that has not been defeated.")
        elif self.revival_tokens == 0:
            print("You are out of revival tokens and cannot revive any more dinosaurs.")

    #Allows a player to check how many revival toekns they have left.
    def __repr__(self):
        return "You have {tokens} revival tokens remaining.".format(tokens = self.revival_tokens)

#The start of what will display in the terminal.

#Variables that will contain the names of the dinosaurs designated by the player.
trex_name = input("Welcome to Dino Duel, Player 1. Player 1 you are the two T-rexes. Player 1, what would you like the name of your first t-rex to be? ").title()
trex2_name = input("Player 1, what would you like the name of your second t-rex to be? ").title()
stego_name = input("Welcome to Dino Duel, Player 2. Player 2 you are the Stegosaruses. Player 2, what would you like the name of your first stegosaurus to be? ").title()
stego2_name = input("Player 2, what would you like the name of your second stegosaurus to be? ").title()

#Creating the dinosaur objects that will duel.
trex1 = Dinosaur(120, 20, 600, trex_name, "t-rex")
stegosaurus1 = Dinosaur(40, 60, 1000, stego_name, "stegosarus")
trex2 = Dinosaur(150, 30, 650, trex2_name, "t-rex")
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

#Using cowsay without the print function allows the input included after cowsay to be displayed in the terminal using the 
#appropriate animal. Including print() before cowsay will result in "none" being printed after the text art as print(cowsay()) would expect
#an output string by using print(cowsay.get_output_string('animal', 'text to output'))
cowsay.trex("The first t-rex is named " + trex_name)
cowsay.trex("The second t-rex is named " + trex2_name)
cowsay.stegosaurus("The first stegosarus is named " + stego_name)
cowsay.stegosaurus("The second stegosarus is named " + stego2_name)

#Simulating a battle below:

#testing checking dinosaur stats before duel begins
print(trex1)
print(stegosaurus1)
print(trex2)
print(stegosaurus2)

#testing checking tokens before any tokens are used
print(player_one)
print(player_two)

#testing active dinosaur function with all dinosaurs active
player_one.check_active_dinosaurs(player_one_dino_list, player_one_defeated_dinos)
player_two.check_active_dinosaurs(player_two_dino_list, player_two_defeated_dinos)

#testing defeated dinosaur function with no dinosaurs defeated
player_one.check_defeated_dinosaurs(player_one_defeated_dinos, player_one_dino_list)
player_two.check_defeated_dinosaurs(player_two_defeated_dinos, player_two_dino_list)

#testing deal damage and lose health functions
trex2.lose_health(stegosaurus1.deal_damage(trex2))
trex1.lose_health(stegosaurus2.deal_damage(trex1))

stegosaurus1.lose_health(trex1.deal_damage(stegosaurus1))
stegosaurus2.lose_health(trex2.deal_damage(stegosaurus2))

#testing revive dinosaur function before a dinosaur can be revived
player_two.revive_dinosaur(stegosaurus1)

#testing heal self function
trex1.heal_self()
trex2.heal_self()

stegosaurus1.heal_self()
stegosaurus2.heal_self()

#Defeating a dinosaur to test revive dinosaur function
trex1.lose_health(stegosaurus2.deal_damage(trex1))
trex1.lose_health(stegosaurus2.deal_damage(trex1))
trex1.lose_health(stegosaurus2.deal_damage(trex1))
trex1.lose_health(stegosaurus2.deal_damage(trex1))
trex1.lose_health(stegosaurus2.deal_damage(trex1))
trex1.lose_health(stegosaurus2.deal_damage(trex1))
trex1.lose_health(stegosaurus2.deal_damage(trex1))
trex1.lose_health(stegosaurus2.deal_damage(trex1))
trex1.lose_health(stegosaurus2.deal_damage(trex1))

#testing check defeated dinosaurs to confirm an error is not given after a dinosaur is revived. This test is used to confirm the
#dinosaur was on the defeated list and is successfully removed after it is revived.
player_one.check_defeated_dinosaurs(player_one_defeated_dinos, player_one_dino_list)

#testing revive dinosaur function for Player 1 and checking if the revival tokens subtract successfully
player_one.revive_dinosaur(trex1)
player_one.revive_dinosaur(trex1)

#testing check defeated dinosaurs to confirm an error is not given after a dinosaur is revived.
player_one.check_defeated_dinosaurs(player_one_defeated_dinos, player_one_dino_list)

#testing checking revival tokens after a token is used
print(player_one)

#Redefeating a dinosaur to test active and defeated list when a dinosaur is defeated
trex1.lose_health(stegosaurus2.deal_damage(trex1))
trex1.lose_health(stegosaurus2.deal_damage(trex1))
trex1.lose_health(stegosaurus2.deal_damage(trex1))
trex1.lose_health(stegosaurus2.deal_damage(trex1))
trex1.lose_health(stegosaurus2.deal_damage(trex1))

#testing check active dinosaurs after a dinosaur is defeated
player_one.check_active_dinosaurs(player_one_dino_list, player_one_defeated_dinos)

#testing check defeated dinosaurs after a dinosaur is defeated
player_one.check_defeated_dinosaurs(player_one_defeated_dinos, player_one_dino_list)

#defeating a dinosaur from player two:
stegosaurus2.lose_health(trex2.deal_damage(stegosaurus2))
stegosaurus2.lose_health(trex2.deal_damage(stegosaurus2))
stegosaurus2.lose_health(trex2.deal_damage(stegosaurus2))
stegosaurus2.lose_health(trex2.deal_damage(stegosaurus2))
stegosaurus2.lose_health(trex2.deal_damage(stegosaurus2))
stegosaurus2.lose_health(trex2.deal_damage(stegosaurus2))
stegosaurus2.lose_health(trex2.deal_damage(stegosaurus2))
stegosaurus2.lose_health(trex2.deal_damage(stegosaurus2))
stegosaurus2.lose_health(trex2.deal_damage(stegosaurus2))
stegosaurus2.lose_health(trex2.deal_damage(stegosaurus2))
stegosaurus2.lose_health(trex2.deal_damage(stegosaurus2))
stegosaurus2.lose_health(trex2.deal_damage(stegosaurus2))
stegosaurus2.lose_health(trex2.deal_damage(stegosaurus2))
stegosaurus2.lose_health(trex2.deal_damage(stegosaurus2))
stegosaurus2.lose_health(trex2.deal_damage(stegosaurus2))
stegosaurus2.lose_health(trex2.deal_damage(stegosaurus2))
stegosaurus2.lose_health(trex2.deal_damage(stegosaurus2))
stegosaurus2.lose_health(trex2.deal_damage(stegosaurus2))
stegosaurus2.lose_health(trex2.deal_damage(stegosaurus2))
stegosaurus2.lose_health(trex2.deal_damage(stegosaurus2))
stegosaurus2.lose_health(trex2.deal_damage(stegosaurus2))
stegosaurus2.lose_health(trex2.deal_damage(stegosaurus2))
stegosaurus2.lose_health(trex2.deal_damage(stegosaurus2))
stegosaurus2.lose_health(trex2.deal_damage(stegosaurus2))
stegosaurus2.lose_health(trex2.deal_damage(stegosaurus2))
stegosaurus2.lose_health(trex2.deal_damage(stegosaurus2))
stegosaurus2.lose_health(trex2.deal_damage(stegosaurus2))
stegosaurus2.lose_health(trex2.deal_damage(stegosaurus2))

#testing checking defeated dinosaurs before checking the active list
player_two.check_defeated_dinosaurs(player_two_defeated_dinos, player_two_dino_list)
player_two.check_active_dinosaurs(player_two_dino_list, player_two_defeated_dinos)

#defeating all dinosuars for a player to test the check active and defeated dinosaurs after no active dinosaurs remain
stegosaurus1.lose_health(trex1.deal_damage(stegosaurus1))
stegosaurus1.lose_health(trex1.deal_damage(stegosaurus1))
stegosaurus1.lose_health(trex1.deal_damage(stegosaurus1))
stegosaurus1.lose_health(trex1.deal_damage(stegosaurus1))
stegosaurus1.lose_health(trex1.deal_damage(stegosaurus1))
stegosaurus1.lose_health(trex1.deal_damage(stegosaurus1))
stegosaurus1.lose_health(trex1.deal_damage(stegosaurus1))
stegosaurus1.lose_health(trex1.deal_damage(stegosaurus1))
stegosaurus1.lose_health(trex1.deal_damage(stegosaurus1))
stegosaurus1.lose_health(trex1.deal_damage(stegosaurus1))
stegosaurus1.lose_health(trex1.deal_damage(stegosaurus1))
stegosaurus1.lose_health(trex1.deal_damage(stegosaurus1))
stegosaurus1.lose_health(trex1.deal_damage(stegosaurus1))
stegosaurus1.lose_health(trex1.deal_damage(stegosaurus1))
stegosaurus1.lose_health(trex1.deal_damage(stegosaurus1))
stegosaurus1.lose_health(trex1.deal_damage(stegosaurus1))
stegosaurus1.lose_health(trex1.deal_damage(stegosaurus1))
stegosaurus1.lose_health(trex1.deal_damage(stegosaurus1))

player_two.check_active_dinosaurs(player_two_dino_list, player_two_defeated_dinos)
player_two.check_defeated_dinosaurs(player_two_defeated_dinos, player_two_dino_list)

#testing heal self function afte a dinosaur is defeated
stegosaurus1.heal_self()

#testing revive dinosaur function for Player 2 and rechecking if the revival tokens subtract successfully
player_two.revive_dinosaur(stegosaurus1)
player_two.revive_dinosaur(stegosaurus1)

#testing checking dinosaur stats after duel is over
print(trex1)
print(stegosaurus1)
print(trex2)
print(stegosaurus2)

#testing checking revival tokens after all tokens have been used for all players
print(player_one)
print(player_two)