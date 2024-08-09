# import json
import requests
import sys


def do(a, b):
    response = requests.get(
        f"https://itunes.apple.com/search?entity=song&limit={a}&term={b}")
    obj = response.json()
    for result in obj['results']:
        print(result['trackName'])


try:
    do(sys.argv[1], sys.argv[2])
except IndexError:
    try:
        number = int(input("Enter number of searches: "))
    except ValueError:
        number = 25
    title = input("Enter name of artist/band: ")
    do(number, title)

'''
print(json.dumps(response.json(), indent=4))
'''
