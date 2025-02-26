from app.models.creatures.human.white.base_white import WhiteHuman

class WhiteWoman(WhiteHuman)
    def __init__(self, name, x_coord, y_coord, z_coord, width, height, z, icon, color, voice):
        super().__init__(name, x_coord, y_coord, z_coord, width, height, z, icon)
        self.skin = color