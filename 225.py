#Write a Python function called describe_pet
# that takes two keyword arguments: animal_type and pet_name.
# The function should print a sentence describing
# the pet in the format: "I have a [animal_type] named [pet_name]."
# Call the function with the arguments animal_type="dog" and pet_name="Buddy".


#I have a dog named Buddy.


def describe_pet(animal_type,pet_name):
    print(f"i have a {animal_type} named {pet_name}")

describe_pet(animal_type="dog",pet_name="buddy")