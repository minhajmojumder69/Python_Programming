
# {'key': 'value','key': 'value'}
person = {'name': 'Sonadhor','address': 'dhonpur','age': 69,'job':'fucker'}
print(person)
print(person['job'])
print(person.keys())
print(person.values())
person['language'] = 'python'

# special dictionary looping
for key,value in person.items():
    print(key,value)