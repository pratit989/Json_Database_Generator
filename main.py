import json


class DataHandler:
    def __init__(self):
        self.f = open('data.json', 'r')
        read_data = self.f.read()
        self.data = json.loads(read_data)
        self.f.close()
        self.selected = None

    def add_data(self, dictionary: dict):
        key = str(input("Enter the key that you want to add: "))
        yes_no = ''
        while yes_no != 'yes' and yes_no != 'no':
            yes_no = str(input("Do you want to add more keys to the key?\n")).lower()
        if yes_no == 'yes':
            try:
                value = dictionary[key]
            except KeyError:
                value = [{}]
            add = 'yes'
            while add == 'yes':
                value[0].update(self.add_data(value[0]))
                add = ''
                while add != 'yes' and add != 'no':
                    add = str(input("Do you want to add more keys?\n")).lower()
            dictionary[key] = value
            print(dictionary)
            return dictionary
        elif yes_no == 'no':
            multi = ''
            value = ''
            while multi != 'yes' and multi != 'no':
                multi = str(input("Do you want to add multiple values?\n")).lower()
                value = str(input("Enter the value for your defined key: "))
            if multi == 'yes':
                value = []
                value = value.append(str(input("Enter the value for your defined property: ")))

            dictionary[key] = value
            print(dictionary)
            return dictionary

    def view_data(self):
        print(json.dumps(self.data, indent=4))

    def write_data(self):
        with open('data.json', 'w') as self.f:
            json.dump(self.data, self.f)


handler = DataHandler()  # Creates instance of the data handler class
handler.view_data()  # Reads data from data.json file and prints it
handler.add_data(handler.data)  # Runs add_data() function to add data
handler.view_data()  # Runs view_data() function to read and print changes
handler.write_data()  # Commits changes to data.json file
