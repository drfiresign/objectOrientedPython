from character import Character
from monster import Dragon
from monster import Goblin
from monster import Troll


class Game:
    def setup(self):
        self.player = Character()
        self.monsters = [
        Goblin(),
        Troll(),
        Dragon()
        ]
        self.monster = self.get_next_monster()


    def get_next_monster(self):
        try:
            return self.monsters.pop(0)
        except IndexError:
            return none


    def monster_turn(self):
        # check to see if the monster attackes
        if self.monster.attack():
        # if so, tell player
            print("You're being attacked!")
            # check if the player wants to dodge
            d = input("Do you want to dodge? [Y]es or [N]o?\n")
            # if so, see if the dodge is sucessful
                if d.lower() == 'y'
                    if self.player.dodge():
                        print("You dodged!")
                        print("What a lucky break!")
                        continue
                    else:
                        print("Your dodge failed and you were attacked")
                        self.player.hit_points -= 1
                        self.player.print_hp()
                else:
                    print("Unless you've accepted death, you should ALWAYS dodge!")
                    print("You were attacked! Idiot...")
                    self.player.hit_points -= 1
                    self.player.print_hp()
                # if it is, move on
            # if it's not, remove one player hit point
        # if the monster isn't attacking, tell the player
        else:
            print("The monster was confused, and mistook you for a tree.")


    def player_turn(self):
        # let the player attack, rest or quit
        action = input("Would you like to [A]ttack, [R]est or [Q]uit?")
        # if they attack
        if action == "a":
            # see if it's sucessful
            if self.player.attack():
                # see if the monster dodged
                if self.monster.dodge():
                    # if dodged, print that
                    print("The {} dodged your attack!".format(self.monster))
                    continue
                # if not dodged, subtrace num of hit points from monster
                else:
                    self.monster.hit_points -= 1
            # if not a good attack, tell the player
            else:
                print("You were too scared to attack this turn.")
        # if they rest:
        elif action == "r":
            # call the player.rest() method
            player.rest()
        elif action == "q":
            print("Quitting now. Thanks for visiting!")
            break
        # if they quit, exit the game
        # if they pick anything else rerun this method
        else:
            self.player_turn()

    def cleanup(self):
        # if the monster has no more hit points:
        if self.monster.hit_points <= 0:
            # up the player's experience
            self.player.experience += 1
            # print a message
            print("Congratulations! You defeated the {}!\nYou've gained 1 experience too!".format(self.monster))
            # get a new monster
            self.monster = self.get_next_monster()


    def __init__(self):
        self.setup()

        while self.player.hit_points and (self.monster or self.monsters):
            print(self.player)
            self.monster_turn()
            self.player_turn()
            self.cleanup()

        if self.player.hit_points:
            print("You Win!")
        elif self.monsters or self.monster:
            print("You Lose!")
