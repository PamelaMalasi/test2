x = [[5, 2, 3], [15, 8, 9]]
students = [
    {'first_name': 'Michael', 'last_name': 'Bryant'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Andres', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 30}]

#2
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(students):
    for n in students:
        print('first name -',n['first_name'],',',' last name -',n['last_name'])

print(iterateDictionary(students))
     
     #3
def iterateDictionary2(key_name, some_list):
    for n in students:
        print(n[key_name])

print(iterateDictionary2('first_name', students))
print(iterateDictionary2('last_name', students))

#4
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for k, v in some_dict.items():
        print(f"{len(v)}, {k.upper()}")
        for i in v:
            print(i)
        print()

printInfo(dojo)
