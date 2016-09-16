from character import Character
from monster import Dragon
from monster import Goblin
from monster import Troll
from sys import exit


class Game:
    def setup(self):
        self.player = Character()
        self.monsters = [Goblin(), Troll(), Dragon()]
        self.monster = self.get_next_monster()

    def get_next_monster(self):
        try:
            return self.monsters.pop(0)
        except IndexError:
            return None

    def monster_turn(self):
        if self.monster.attack():
            print("{} is attacking!".format(self.monster))
            d = input("Dodge? Y/N ").lower()
            if d == 'y':
                if self.player.dodge():
                    print("You dodged the attack!")
                    print("What a lucky break!")
                else:
                    print("You got hit anyway!")
                    self.player.hit_points -= 1
                    self.player.print_hp()
            else:
                print("Unless you've accepted death, you should ALWAYS dodge!")
                print("{} hit you for 1 point!".format(self.monster))
                self.player.hit_points -= 1
                self.player.print_hp()
        else:
            print("{} isn't attacking this turn.".format(self.monster))

    def player_turn(self):
        action = input("Would you like to [A]ttack, [R]est or [Q]uit?").lower()
        if action == "a":
            print("You're attacking {}!".format(self.monster))
            if self.player.attack():
                if self.monster.dodge():
                    print("{} dodged your attack!".format(self.monster))
                else:
                    if self.player.leveled_up():
                        self.monster.hit_points -= 2
                    else:
                        self.monster.hit_points -= 1
                    print("You hit {} with your {}".format(self.monster,
                                                           self.player.weapon))
            else:
                print("You missed!")
        elif action == "r":
            self.player.rest()
        elif action == "q":
            print("Quitting now. Thanks for visiting!")
            exit()
        else:
            self.player_turn()

    def cleanup(self):
        if self.monster.hit_points <= 0:
            self.player.experience += self.monster.experience
            print("Congratulations! You defeated {}!".format(self.monster))
            print("You've gained {} experience too!".format(
                self.monster.experience))
            self.monster = self.get_next_monster()

    def __init__(self):
        self.setup()
        while self.player.hit_points and (self.monster or self.monsters):
            print("\n" + "=" * 20)
            print(self.player)
            self.monster_turn()
            print('-' * 20)
            self.player_turn()
            self.cleanup()
            print("\n" + "=" * 20)

        if self.player.hit_points:
            print("You Win!")
        elif self.monsters or self.monster:
            print("You Lose!")
            exit()


Game()
