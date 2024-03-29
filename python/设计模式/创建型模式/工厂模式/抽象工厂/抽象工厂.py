# Author: Jason Lu
class Frog:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        print('{} the Frog encounters {} and {}'.format(self.name, obstacle, obstacle.action()))


class Bug:
    def __str__(self):
        return 'a4 bug'

    def action(self):
        return 'eats it'


class FrogWorld:
    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return '\n\n\t-------- Frog Wrold --------'

    def make_character(self):
        return Frog(self.player_name)

    def make_obstacle(self):
        return Bug()


##########################################################

class Wirzard:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        print('{} the Wizard battles against {} and {}'.format(self.name, obstacle, obstacle.action()))


class Ork:
    def __str__(self):
        return 'an evil ork'

    def action(self):
        return 'kills it'


class WizardWorld:
    def __int__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return '\n\n\t-------- Wizard World --------'


    def make_character(self):
        return Wirzard(self.player_name)

    def make_obstacle(self):
        return Ork()


##########################################################


class GameEnvironment:
    def __init__(self, factory):
        self.hero = factory.make_character()
        self.obstacle = factory.make_obstacle()

    def play(self):
        self.hero.interact_with(self.obstacle)


def validate_age(name):
    try:
        age = input('Welcome {}. How old are you?'.format(name))
        age = int(age)
    except ValueError as err:
        print('Age {} is inavlid, please try again....'.format(age))
        return (False, age)

    return (True, age)


def main():
    name = input("Hello, What's your name?")
    vaild_input = False
    while not vaild_input:
        vaild_input, age = validate_age(name)

    game = FrogWorld if age < 18 else WizardWorld
    environment = GameEnvironment(game(name))
    environment.play()


##########################################################


if __name__ == '__main__':
    main()













