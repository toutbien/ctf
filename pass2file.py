#This is a password cracking file intended to combine seperate files into one list for cracking hashes, built with Python

def read_file(file_name):
    with open(file_name, 'r') as file:
        return [line.strip() for line in file]

def combine_words(animal_file, num_file):
    animals = read_file(animal_file)
    numbers = read_file(num_file)

    combinations = []
    for animal in animals:
        for num in numbers:
            combinations.append(animal + num)
    return combinations

# Use the function
combinations = combine_words('comb2', 'nmb')

# Write the combinations to a file
with open('passwd2', 'w') as file:
    for combo in combinations:
        file.write(combo + '\n')
