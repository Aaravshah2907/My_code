import sys
import json
import clipboard

SAVED_DATA = 'pswd.json'


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


def update(key):
    if f'{key}_old' not in data:
        data[f'{key}_old'] = data[key]
    else:
        if data[key] == data[f'{key}_old']:
            pass
        else:
            update(f'{key}_old')
            data[f'{key}_old'] = data[key]


if len(sys.argv) == 2:
    command = sys.argv[1][0]

else:
    command = ''

data = read_items(SAVED_DATA)

if command == 's' or command == '1':
    key = input('Enter a key: ')
    if key not in data:
        data[key] = clipboard.paste()
        save_items(SAVED_DATA, data)
        print('Data Saved')
    else:
        dec = input(
            'Key already exists. Do you want to change the existing key value? (y/n)')
        if dec[0].lower() == 'y':
            update(key)
            data[key] = clipboard.paste()
            save_items(SAVED_DATA, data)
            print('Data Saved')
        else:
            print('Command Cancelled')
elif command == 'c' or command == '2':
    key = input('Enter a key: ')
    if key in data:
        if len(clipboard.paste()) < 1:
            clipboard.copy(data[key])
            print("Data Copied to clipboard")
        else:
            dec = input(
                'There is a string attached to your clipboard.\nDo you want to continue with exchanging the clipboard value? (y/n)').lower()
            if dec[0] == 'y':
                clipboard.copy(data[key])
                print("Data Copied to clipboard")
            else:
                print("Command Cancelled")
    else:
        print("Data doesn't exist")
elif command == 'k' or command == '3':
    for key in data:
        print(f'{key}, ', end='')
    print("")
elif command == 'h' or command == '4':
    print("Commands Include: \n1. save - saves data from clipboard\n2. copy - copy data to clipboard\n3. keys - display keys available\n4. help - displays this message :)")
    sys.exit()
else:
    print('Unknown Command')
