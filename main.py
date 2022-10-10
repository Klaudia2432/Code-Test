import random

def remove_duplicates_and_sort_desc(list_of_digits: list) -> list:
    # Delete duplications from the list
    new_list = remove_duplicates(list_of_digits)
    # Sort list in descending order
    new_list.sort(reverse=True)
    return new_list

def remove_duplicates(list_of_digits: list) -> list:
    new_list = []
    for n in list_of_digits:
        if n not in new_list:
            new_list.append(n)
    return new_list

def generate_list_of_digits() -> list:
    digits = []
    for i in range(0,10):
        n = random.randint(1,100)
        digits.append(n)
    return digits

# CODE EXAMPLE


print("OPTION ONE (Hard coded list): ")
digits = [1, 2, 2, 4, 5, 6, 7, 8, 9, 9]
print(remove_duplicates_and_sort_desc(digits))

# Read the randomly generated list
print("OPTION TWO (Randomly generated list): ")
digits = generate_list_of_digits();
print(remove_duplicates_and_sort_desc(digits))