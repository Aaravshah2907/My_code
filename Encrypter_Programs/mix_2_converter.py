import encrypter2
import csv

database_list = []
database_dict = {}
username = input("Enter Username: ")
password = input("Enter Password: ")
key = input("Key: ")
hash = encrypter2.main(0, password, key)

with open("database1.csv", 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        database_list.append({ "username": row['username'] , "password": row['password'], "hc":row["hash_code"], "key":row["key"]})

database_list.append({'username':username, "password":password, "hc":hash, 'key':key})

for element in database_list:
    database_dict[element['username']] = [element['key'], element['password'] , element['hc']]

with open('database1.csv', 'a', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['username','key','password',"hash_code"])
    writer.writerow({'username': username, 'key': key,'password': password, "hash_code": hash})
