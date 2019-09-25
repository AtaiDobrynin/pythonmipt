import os
import csv


class CarBase:
    def __init__(self, car_type, brand, photo_file_name, carrying):
        self.car_type = car_type
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying
    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]
 
 
class Car(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(car_type, brand, photo_file_name, carrying)
        self.passenger_seats_count = passenger_seats_count


class Truck(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, body_length, body_width, body_height):
        super().__init__(car_type, brand, photo_file_name, carrying)
        self.body_length = body_length
        self.body_width = body_width
        self.body_height = body_height
    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height

		
class SpecMachine(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, extra):
        super().__init__(car_type, brand, photo_file_name, carrying)
        self.extra = extra

                
def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            if len(row) < 7:
                pass
            print(row[0])
            if row[0] == 'car':
                if row[1] == '' or row[3] == '' or row[5] == '' or row[2] == '':
                    pass
                car1 = Car(row[0], row[1], row[3], row[5], int(row[2]))
                car_list.append(car1)
            if row[0] == 'truck':
                if row[1] == '' or row[3] == '' or row[5] == '':
                    pass
                if row[4] == '':
                    s[0], s[1], s[2] = 0, 0, 0
                else:
                    s = [float(i) for i in row[4].strip().split('x')]
                print(s)
                car1 = Truck(row[0], row[1], row[3], row[5], s[0], s[1], s[2])
                car_list.append(car1)
            if row[0] == 'spec_machine':
                if row[1] == '' or row[3] == '' or row[5] == '' or row[6] == '':
                    pass
                car1 = SpecMachine(row[0], row[1], row[3], row[5], row[6])
                car_list.append(car1)
            if row[0] == '':
                pass
    return car_list