from vehicle_manager_model import VehiclesManager


def program():
    print "Welcome to your Vehicle Manager!"

    manager = VehiclesManager()
    manager.load_from_file()

    choice = ''
    while choice != 'e':
        print ""
        print "Please pick one of the following options:"
        print "a) See a list of all the company vehicles."
        print "b) Add new vehicle."
        print "c) Add kilometers done for the chosen vehicle."
        print "d) Edit the last service date for the chosen vehicle."
        print "e) Quit the program."
        print ""

        choice = raw_input("Which option would you like to choose? (a, b, c, d, e): ").lower()
        print ""

        if choice == "a":
            manager.list_all_vehicles()
        elif choice == "b":
            manager.add_new_vehicle()
        elif choice == "c":
            manager.add_vehicle_kilometers()
        elif choice == "d":
            manager.update_vehicle_service_date()
        elif choice == "e":
            manager.save_to_file()
        else:
            print "Wrong choice. Please type in just a letter, either a, b, c, d or e."

    print "Thank you for using the Vehicle Manager. Have a nice day!"


if __name__ == '__main__':
    program()
