import sys
import json
import clipboard


SAVED_DATA = 'clipboard.json'
def save_items(filepath, data):
    with open(filepath, 'w') as file:
        json.dump(data, file)
        
        
def read_items(filepath):
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            return data
    except:
        return {}


if len(sys.argv) == 2:
    command = sys.argv[1]
    data = read_items(SAVED_DATA)
    
    if command == 'save':
        key = input('Enter a key: ')
        data[key] = clipboard.paste()
        save_items(SAVED_DATA,data)
        print('Data Saved')
    elif command == 'load':
        key = input('Enter a key: ')
        if key in data:
            clipboard.copy(data[key])
            print("Data Copied to clipboard")
        else:
            print("Data doesn't exist")
    elif command == 'list':
        print(data)
    else:
        print('Unknown Commmand')
else:
    print("Pass 2 Arguements")