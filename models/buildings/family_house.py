from app.models.buildings.base_building import BaseBuilding

class FamilyHouse(BaseBuilding):
    def __init__(self, name, x_coord, y_coord, z_coord, width, height, z, icon, capacity, color, doors, windows, garden_width, garden_height):
        super().__init__(name, x_coord, y_coord, z_coord, width, height, z, icon, capacity, color, doors, windows)
        self.garden_width = garden_width
        self.garden_height = garden_height