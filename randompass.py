import random
import string

def gen_password(length, letters=True, numbers=True, symbols=True):
    characters = ''
    if letters:
        characters += string.ascii_letters  
    if numbers:
        characters += string.digits        
    if symbols:
        characters += string.punctuation    

    if not characters:
        raise ValueError("You must select at least one character type!")

    password_chars = []
    for i in range(length):
        random_char = random.choice(characters)
        password_chars.append(random_char)

    password = ''.join(password_chars)
    return password

def main():
    print("=== Password Generator ===")

    while True:
        try:
            length = int(input("Enter password length: "))
            if length <= 0:
                print("Length must be a positive integer.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    letters = input("Include letters? (y/n): ").strip().lower() == 'y'
    numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
    symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'

    try:
        password = gen_password(length, letters, numbers, symbols)
        print(f"\nGenerated password: {password}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()