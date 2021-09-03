import random

def password_generator():
    UPPERCASE = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    LOWERCASE = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    NUM = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    CHAR = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']

    #plus all characters
    characters = UPPERCASE + LOWERCASE + NUM + CHAR

    #list
    password = []

    for i in range(15):
        random_characters = random.choice(characters)
        password.append(random_characters)

    #become the list to string
    password = "".join(password)

    return password


def run():
    password = password_generator()
    print('Your new password is: ' + password)


if __name__ == '__main__':
    run()