import os


class File:
	def __init__(self, path):
		self.path = path
		self.current_position = 0
		
		if not os.path.exists(self.path):
			open(self.path, 'w').close()
	
	def __str__(self):
		return self.path
	
	def write(self, string):
		with open(self.path, 'w') as ouf:
			return ouf.write(string)

			
file1 = File("example.txt")
print(file1)