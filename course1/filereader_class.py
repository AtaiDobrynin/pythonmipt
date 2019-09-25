class FileReader():
	def __init__(self, path):
		self.path = path
	def read(self):
		try:
			with open(self.path, 'r') as inf:
				result = inf.read()
			return result
		except IOError:
			return ""
'''
reader = FileReader("example.txt")
print(reader.read())
'''