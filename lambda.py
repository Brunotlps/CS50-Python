people = [
    {"name": "Hary", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

print(people)



people.sort(key=lambda person: person["name"])

print(people)