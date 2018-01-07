from datetime import datetime
from vehicle_model import Vehicle


class VehiclesManager(object):
    def __init__(self):
        self.vehicles = []

    def list_all_vehicles(self):
        if len(self.vehicles) > 0:
            print "Company vehicles:"
            for index, vehicle in enumerate(self.vehicles):
                print "{}. {}".format(index + 1, vehicle.get_str_data())

        else:
            print "There is no vehicle yet."

    def add_new_vehicle(self):
        brand = raw_input("Please enter the brand of the vehicle: ")
        model = raw_input("Please enter the model of the vehicle: ")
        km_done_str = raw_input("Please enter the amount of kilometers that vehicle has done so far (number): ")
        service_date = raw_input("Please enter the last service date (DD/MM/YYYY): ")

        vehicle_object = self.create_vehicle_object(brand, model, km_done_str, service_date)

        if vehicle_object:
            print "You have successfully added a new vehicle: {}!".format(vehicle_object.get_str_data())
        else:
            print "Something went wrong"

    def add_vehicle_kilometers(self):
        vehicle = self.choose_vehicle()
        print "Vehicle selected: {} with {} km".format(vehicle, vehicle.kilometers)
        print ""
        new_km_str = raw_input("How many kilometers would you like to add to the existing ones? (number) ")
        print ""

        try:
            new_km = float(new_km_str)
            vehicle.add_kilometers(new_km)
            print "New number of kilometers for {} is now: {}".format(vehicle, vehicle.kilometers)
        except ValueError:
            print "You entered a wrong value"

    def update_vehicle_service_date(self):
        vehicle = self.choose_vehicle()
        print "Vehicle selected: {} with service date {}".format(vehicle, vehicle.get_service_date_formatted())
        print ""
        new_service_date_str = raw_input("What is the new service date for this vehicle? (DD/MM/YYYY) ")
        print ""

        try:
            new_service_date = datetime.strptime(new_service_date_str, '%d/%m/%Y')
            vehicle.update_service_date(new_service_date)
            print "Service date for {} is now: {}".format(vehicle, vehicle.get_service_date_formatted())
        except ValueError:
            print "You entered a wrong date format"

    def create_vehicle_object(self, brand, model, kilometers_str, service_date_str):
        try:
            kilometers = float(kilometers_str)
            service_date = datetime.strptime(service_date_str, '%d/%m/%Y')

            new_vehicle = Vehicle(brand, model, kilometers, service_date)
            self.vehicles.append(new_vehicle)

        except ValueError:
            new_vehicle = None

        return new_vehicle

    def choose_vehicle(self):
        self.list_all_vehicles()
        print ""
        selection = raw_input("What vehicle number wold you like to choose? ")
        return self.vehicles[int(selection) - 1]

    def save_to_file(self):
        with open("vehicles.txt", "w+") as vehicles_file:
            for vehicle in self.vehicles:
                vehicles_file.write(vehicle.get_csv_data())
                vehicles_file.write('\n')

    def load_from_file(self):
        with open("vehicles.txt", "r") as vehicles_file:
            for vehicle_data in vehicles_file:
                brand, model, km, date = vehicle_data.strip().split(",")
                self.create_vehicle_object(brand, model, km, date)
