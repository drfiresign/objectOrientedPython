class Monster():
    """Instance of Monster.

    Dislikes fire."""
    hit_points = 1
    color = 'yellow'
    weapon = 'sword'
    sound = 'roar'

    def battlecry(self):
        return self.sound.upper()
