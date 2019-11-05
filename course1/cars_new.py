import csv
import os


class CarBase():
	def __init__(self, brand, photo_file_name, carrying):
		self.photo_file_name = photo_file_name
		self.brand = brand
		self.carrying = carrying
		
	def get_photo_file_ext(self):
		return os.path.splitext(self.photo_file_name)[1].replace(".","")

		
class Car(CarBase):
	car_type = "car"
	
	def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
		super().__init__(brand, photo_file_name, carrying)
		self.passenger_seats_count = passenger_seats_count


class Truck(CarBase):
	car_type = "truck"
	
	def __init__(self, brand, photo_file_name, carrying, body_whl):
		super().__init__(brand, photo_file_name, carrying)
		try:
			dims = [float(i) for i in body_whl.split("x")]	
		except ValueError:
			dims = [0.0, 0.0, 0.0]
		self.body_width = dims[0]
		self.body_height = dims[1]
		self.body_length = dims[2]
		
	def get_body_volume(self):
		return self.body_height * self.body_width * self.body_length

		
class SpecMachine(CarBase):
	car_type = "spec_machine"
	def __init__(self, brand, photo_file_name, carrying, extra):
		super().__init__(brand, photo_file_name, carrying)
		self.extra = extra


def get_car_list(csv_filename):
	car_list = []
	with open(csv_filename) as csv_fd:
		reader = csv.reader(csv_fd, delimiter=';')
		next(reader) 
		for row in reader:
			if len(row) == 7:
				if row[0] == "car":
					car_list.append(Car(row[1], row[3], row[5], int(row[2])))
				elif row[0] == "truck":
					car_list.append(Truck(row[1], row[3], row[5], row[4]))
				elif row[0] == "spec_machine":
					car_list.append(SpecMachine(row[1], row[3], row[5], row[6]))
	return car_list
