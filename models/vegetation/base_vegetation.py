from app.models.base_entity_class import BaseEntity

class Vegetation(BaseEntity):
    def __init__(self, name, x_coord, y_coord, z_coord, width, height, z, icon, color1, color2, color3):
        super().__init__(name, x_coord, y_coord, z_coord, width, height, z, icon)
        self.color1 = color1
        self.color2 = color 2
        self.color3 = color 3