class MappingAdapter:
	def __init__(self, adaptee):
		self.adaptee = adaptee

	def lighten(self, grid):
		self.adaptee.set_dim((len(grid[0]), len(grid)))
		lights = list()
		obstacles = list()
		for i in range(self.adaptee.dim[0]):
			for j in range(self.adaptee.dim[1]):
				if grid[j][i] == 1:
					lights.append((i, j))
				elif grid[j][i] == -1:
					obstacles.append((i, j))
		self.adaptee.set_lights(lights)
		self.adaptee.set_obstacles(obstacles)
		return self.adaptee.grid
		
		
