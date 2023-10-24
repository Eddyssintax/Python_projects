import random

def generate_password(length):
    characters = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVNM1234567890!@#$%^&*_'
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    quantity = int(input("How many passwords do you need: "))
    length = int(input("Enter password length: "))

    if length < 8:
        print("Warning! Password must be 8+ characters in length.")
    else:
        for x in range(1, quantity + 1):
            password = generate_password(length)
            print(f"Password {x}: {password}")

if __name__ == "__main__":
    main()