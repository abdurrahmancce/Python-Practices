person = {
    'name': 'Abdur Rahman',
    'age': 24,
    'city': 'Chittagong',
    'occupation': 'Engineer'
}

print(person)

person['age'] = 25               # Modifying the 'age' value
person['city'] = 'Dhaka'         # Modifying the 'city' value
person['occupation'] = 'Developer'  # Modifying the 'occupation' value

print(person)
print(f"\nName: {person['name']}")
print(f"Age: {person['age']}")
print(f"City: {person['city']}")
print(f"Occupation: {person['occupation']}")
