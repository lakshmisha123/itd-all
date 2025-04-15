import json

# File path where JSON data is stored
file_path = "data.json"


# Function to load JSON data from file
def load_data():
    with open(file_path, "r") as file:
        return json.load(file)


# Function to save JSON data to file
def save_data(data):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)


# CREATE operation
def create(data):
    existing_data = load_data()
    existing_data.append(data)
    save_data(existing_data)


# READ operation
def read():
    data = load_data()
    return data


# UPDATE operation
def update(index, new_data):
    existing_data = load_data()
    if 0 <= index < len(existing_data):
        existing_data[index] = new_data
        save_data(existing_data)
    else:
        print("Invalid index.")


# DELETE operation
def delete(index):
    existing_data = load_data()
    if 0 <= index < len(existing_data):
        del existing_data[index]
        save_data(existing_data)
    else:
        print("Invalid index.")


# Example usage
create({"name": "John", "age": 30})
create({"name": "Alice", "age": 25})
print("Initial data:")
print(read())

update(0, {"name": "John Doe", "age": 32})
print("\nData after update:")
print(read())

delete(1)
print("\nData after delete:")
print(read())
