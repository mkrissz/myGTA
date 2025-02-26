class BaseEntity:
    def __init__(self, name, x_coord, y_coord, z_coord, width, height, z, icon):
        self.first_name = name
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.z_coord = z_coord
        self.width = width
        self.height = height
        self.z = z
        self.icon = icon
    
    def __str__(self):
        return f'Name: {first_name}, coords: ({x_coord, y_coord, z_coord})'
    
    