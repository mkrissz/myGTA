from app.models.building.flat_building import FlatBuilding

class SkyScraper()
    def __init__(self, name, x_coord, y_coord, z_coord, width, height, z, icon, capacity, color, doors, windows, floors):
        super().__init__(name, x_coord, y_coord, z_coord, width, height, z, icon, capacity, color, doors, windows)
        self.floors = floors