from app.models.creatures.base_creatures import Creatures

class Birds(Creatures)
    def __init__(self, name, x_coord, y_coord, z_coord, width, height, z, icon, color, voice):
        super().__init__(name, x_coord, y_coord, z_coord, width, height, z, icon) 
        self.voice = voice