# Car System Data
car_system_data = {}

# System inserted data base
def add_system_data(system_name):
    system_data = {}
    # retrieve data for the selected system and store it in the dictionary
    # for example, you could prompt the user for input or retrieve the data from a file or database
    # here, we'll just add some sample data for demonstration purposes
    if system_name == "engine":
        system_data["type"] = "V6"
        system_data["horsepower"] = 300
        system_data["fuel_type"] = "gasoline"
    elif system_name == "brakes":
        system_data["type"] = "disc"
        system_data["rotor_size"] = 12.5
        system_data["pad_material"] = "ceramic"
    elif system_name == "audio":
        system_data["brand"] = "Bose"
        system_data["speakers"] = 10
        system_data["subwoofer"] = True
    else:
        print("Invalid system name")
        return
    
    car_system_data[system_name] = system_data
    print("Data for", system_name, "system has been added to the dictionary")

# define a function to print the data for a selected system
def print_system_data(system_name):
    if system_name in car_system_data:
        system_data = car_system_data[system_name]
        print("Data for", system_name, "system:")
        for key, value in system_data.items():
            print(key, ":", value)
    else:
        print("No data found for", system_name, "system")

# prompt the user to select a car system
system_name = input("Enter car system name (engine, brakes, audio): ")

# add the system data to the dictionary
add_system_data(system_name)

# print the data for the selected system
print_system_data(system_name)
