from app.models.vegetation.base_vegetation import Vegetation

class Tree(Vegetation)
    def __init__(self, name, x_coord, y_coord, z_coord, width, height, z, icon, color1, color2, color3):
        super().__init__(name, x_coord, y_coord, z_coord, width, height, z, icon)