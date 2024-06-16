import json


def Choices():
    print("Data Base manger")
    print("(1) View Data")
    print("(2) Add Data")
    print("(3) Delete  Data")
    print("(4) Exit")


def read_json_file():
    filename = "./data/db.json"
    with open(filename, "r") as f:
        temp = json.load(f)
        return temp


def write_json_file(temp):
    filename = "./data/db.json"
    with open(filename, "w") as f:
        json.dump(temp, f, indent = 4)


def view_data():
    temp = read_json_file()
    i = 0
    for entry in temp:
        name = entry["name"]
        appearance = entry["appearance"]
        roll =  entry["roll"]
        key = entry["key"]
        print(f"index number: {i}")
        print(f"name of NPC: {name}")
        print(f"appearance of NPC {appearance}")
        print(f"how to roll play the NPC {roll}")
        print(f"The key info of the NPC {key}")
        print("\n\n")
        i=i+1


def delete_data():
    view_data()
    new_data = []
    temp = read_json_file()
    data_length = len(temp) -1
    print("which item do you want to delete?")
    delete_option = input(f"select a number 0-{data_length}")
    i=0
    for entry in temp:
        if i == int(delete_option):
            pass
            i=i+1
        else:
            new_data.append(entry)
            i=i+1
        write_json_file(new_data)
        




def add_data():
    item_data = {}
    temp = read_json_file()
    item_data["name"] = input("name of NPC")
    item_data["appearance"] = input("appearance of NPC")
    item_data["roll"] = input("how to roll play the NPC")
    item_data["key"] = input("The key info of the NPC")
    temp.append(item_data)
    write_json_file(temp)




while True:
    Choices()
    choice = input("/nEnter Number: ")
    if choice == "1":
        view_data()
    elif choice == "2":
        add_data()
    elif choice == "3":
        delete_data()
    elif choice == "4":
        break
    else:
        print("please make a selection:")




