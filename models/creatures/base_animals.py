from app.models.creatures.base_creatures import Creatures
    
class Four-legged(Creatures) 
    def __init__(self, name, x_coord, y_coord, z_coord, width, height, z, icon, color):
        super().__init__(name, x_coord, y_coord, z_coord, width, height, z, icon)        
