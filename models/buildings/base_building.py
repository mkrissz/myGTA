from app.models.base_entity_class import BaseEntity

class BaseBuilding(BaseEntity):
    def __init__(self, name, x_coord, y_coord, z_coord, width, height, z, icon, capacity, color, doors, windows):
        super().__init__(name, x_coord, y_coord, z_coord, width, height, z, icon)
        self.capacity = capacity
        self.color = color
        self.doors = doors
        self.windows = windows