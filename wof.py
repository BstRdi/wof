from random import choice
"""A class that can be used to represent a wheel of fortune."""


fields = ('FAIL!', 'FAIL!', 100, 'FAIL!', 'FAIL!', 500, 'FAIL!', 250, 'FAIL!', 'FAIL!', 'FAIL!', 'FAIL!', 1000, 'FAIL!', 'FAIL!', 'FAIL!', 'FAIL!', 'FAIL!', 'FAIL!')

score = []

class WheelOfFortune:
    """A simple attempt to represent a wheel of fortune."""

    def __init__(self, fields, spins=10):
        """Initialize attributes to describe a wheel of fortune."""
        self.fields = fields
        self.spins = spins

    def spin_wheel(self):
        """Spin the wheel of fortune"""
        for spin in range(1, self.spins):
            spin = choice(fields)
            print(spin)
            if isinstance(spin, int) == True:
                score.append(spin)
        sum_score = sum(score)
        print(f'{player_name} you got {sum_score} points!')

                
# Spin for player one
player_name = input('Player One - Enter your name: ')
player_one = WheelOfFortune(fields)
player_one.spin_wheel()
player_one_score = score[:]
player_one_name = player_name
del score[:]

# Spin for player two
player_name = input('Player Two - Enter your name: ')
player_two = WheelOfFortune(fields)
player_two.spin_wheel()
player_two_score = score[:]
player_two_name = player_name

# Selection of the winner
if player_one_score > player_two_score:
    print(f'{player_one_name} wins!')
elif player_two_score > player_one_score:
    print(f'{player_two_name} wins!')
elif player_one_score == player_two_score:
    print('Draw!')