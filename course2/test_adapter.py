from adapter_pattern import MappingAdapter


class Light:
	def __init__(self, dim):
		self.dim = dim
		self.grid = [[0 for i in range(dim[0])] for _ in range(dim[1])]
		self.lights = []
		self.obstacles = []
    
	def set_dim(self, dim):
		self.dim = dim
		self.grid = [[0 for i in range(dim[0])] for _ in range(dim[1])]

	def set_lights(self, lights):
		self.lights = lights
		self.generate_lights()

	def set_obstacles(self, obstacles):
		self.obstacles = obstacles
		self.generate_lights()
		
	def generate_lights(self):
		return self.grid.copy()
		

class System:
	def __init__(self):
		self.chart = self.grid = [[0 for i in range(30)] for _ in range(20)]
		self.chart[5][7] = 1 # Источники света
		self.chart[5][2] = -1 # Стены
	
	def get_lightening(self, light_chartper):
		self.lightchart = light_chartper.lighten(self.chart)

		
system = System()
lighter1 = Light((1 ,1))
adapter1 = MappingAdapter(lighter1)
system.get_lightening(adapter1)
