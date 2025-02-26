from app.models.creatures.base_human import Human

class WhiteHuman(Human)
    def __init__(self, name, x_coord, y_coord, z_coord, width, height, z, icon, color, voice):
        super().__init__(name, x_coord, y_coord, z_coord, width, height, z, icon)
        self.skin = color