import json


def Choices():
    print("Data Base manger")
    print("(1) View Data")
    print("(2) Add Data")
    print("(3) Edit Data")
    print("(4) Delete  Data")
    print("(5) Exit")


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
        short_description = entry["short_description"]
        print(f"index number: {i}")
        print(f"the short description is: {short_description}")
        full_description = entry["full_description"]
        for subentry in full_description:
            name = subentry["name"]
            appearance = subentry["appearance"]
            roll =  subentry["roll"]
            key = subentry["key"]
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


def edit_data():
    view_data()
    new_data = []
    temp = read_json_file()
    data_length = len(temp) -1
    print("which item do you want to edit")
    edit_option = input(f"select a number 0 - {data_length}")
    i=0
    for entry in temp:
        if i == int(edit_option):
            short_description = entry["short_description"]
            temp_data = {}
            temp_data["short_description"] = str(input(f"current short_description: {short_description}") or f"{short_description}")
            print(f"index number: {i}")
            print(f"the short description is: {short_description}")
            full_description = entry["full_description"]
            for subentry in full_description:
                name = subentry["name"]
                appearance = subentry["appearance"]
                roll =  subentry["roll"]
                key = subentry["key"]
                new_description = []
                full_temp_data = {}
                full_temp_data["name"] = str(input(f"current name: {name}") or f"{name}")
                full_temp_data["appearance"] = str(input(f"current line: {appearance}") or f"{appearance}")
                full_temp_data["roll"] = str(input(f"current line: {roll}") or f"{roll}")
                full_temp_data["key"] = str(input(f"current line: {key}") or f"{key}")
                new_description.append(full_temp_data)
                temp_data["full_description"] = new_description
                new_data.append(temp_data)
                i=i+1
        else:
            new_data.append(entry)
            i=i+1
        write_json_file(new_data)
    




def add_data():
    temp_data = {}
    item_list = []
    item_data = {}
    temp = read_json_file()
    temp_data["short_description"] = input("description of NPC")
    item_data["name"] = input("name of NPC")
    item_data["appearance"] = input("appearance of NPC")
    item_data["roll"] = input("how to roll play the NPC")
    item_data["key"] = input("The key info of the NPC")
    item_list.append(item_data)
    temp_data["full_description"] =item_list 
    temp.append(temp_data)
    write_json_file(temp)




while True:
    Choices()
    choice = input("/nEnter Number: ")
    if choice == "1":
        view_data()
    elif choice == "2":
        add_data()
    elif choice == "3":
        edit_data()
    elif choice == "4":
        delete_data()
    elif choice == "5":
        break
    else:
        print("please make a selection:")




