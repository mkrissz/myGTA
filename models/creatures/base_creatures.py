from app.models.base_entity_class import BaseEntity

class Creatures(BaseEntity)
    def __init__(self, name, x_coord, y_coord, z_coord, width, height, z, icon, color):
        super().__init__(name, x_coord, y_coord, z_coord, width, height, z, icon)
        self.color = color