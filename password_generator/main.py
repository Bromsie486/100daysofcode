import random


def main():
    number_of_letters = int(input("Welcome to my Password Generator!\n How many letters would you like to include in your password?"))
    number_of_symbols = int(input("How many symbols would you like to include in your password?"))
    number_of_numbers = int(input("How many numbers would you like to include in your password?"))
    password = ""
    password = add_letters_to_password(password, number_of_letters)
    password = add_symbols_to_password(password, number_of_symbols)
    password = add_numbers_to_password(password, number_of_numbers)
    newPassword = create_password(password)
    print(f"Your password is {newPassword}")
    

def add_letters_to_password(password, number_of_letters):
    list_of_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    for i in range(number_of_letters):
        if random.randint(0, 1) == 0:
            password += list_of_letters[random.randint(0, len(list_of_letters)-1)]
        else:
            password += list_of_letters[random.randint(0, len(list_of_letters)-1)].lower()
    return password
    

def add_symbols_to_password(password, number_of_symbols):
    list_of_symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "-", "="]
    for i in range(number_of_symbols):
        password += list_of_symbols[random.randint(0, len(list_of_symbols)-1)]
    return password


def add_numbers_to_password(password, number_of_numbers):
    for i in range(number_of_numbers):
        password += str(random.randint(0, 9))
    return password


def create_password(oldPassword):
    helper_list = []
    for char in oldPassword:
        helper_list.append(char)
    password = ""
    while helper_list != []:
        if len(helper_list) > 1:
            random_number = random.randint(0, len(helper_list)-1)
            password += helper_list[random_number]
            helper_list.pop(random_number)
        else:
            password += helper_list[0]
            helper_list.pop(0)
    return password


if __name__ == "__main__":
    main()
