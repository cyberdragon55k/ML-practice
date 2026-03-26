# json

import json




with open('Jupyter\ex.json','r') as file:
    person = json.load(file)
    print(person)
