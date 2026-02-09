import secrets
import string
import sys

def get_valid_length() -> int:
    
    while True:
        user_input = input("Enter desired password length (e.g., 12): ").strip()
        try:
            length = int(user_input)
            if length > 0:
                return length
            print("Error: Length must be a positive number greater than 0.")
        except ValueError:
            print("Error: Invalid input. Please enter a numeric value.")

def get_boolean_choice(prompt: str) -> bool:
    
    while True:
        response = input(f"{prompt} (y/n): ").lower().strip()
        if response in ['y', 'yes']:
            return True
        elif response in ['n', 'no']:
            return False
        print("Please answer with 'y' or 'n'.")

def generate_password(length: int, use_upper: bool, use_digits: bool, use_symbols: bool) -> str:
    
    character_pool = string.ascii_lowercase
    
    if use_upper:
        character_pool += string.ascii_uppercase
    if use_digits:
        character_pool += string.digits
    if use_symbols:
        character_pool += string.punctuation

    if not character_pool:
        raise ValueError("Character pool is empty.")

    password = ''.join(secrets.choice(character_pool) for _ in range(length))
    
    return password

def main():
    
    print("--- Secure Password Generator ---")
    print("Generate a cryptographically strong password.\n")

    length = get_valid_length()

    print("\n--- Customize Complexity ---")
    use_upper = get_boolean_choice("Include Uppercase letters? (A-Z)")
    use_digits = get_boolean_choice("Include Numbers? (0-9)")
    use_symbols = get_boolean_choice("Include Symbols? (@, #, $, etc.)")

    try:
        password = generate_password(length, use_upper, use_digits, use_symbols)
        print("\n" + "="*30)
        print(f"Generated Password:  {password}")
        print("="*30)
        print(f"Stats: Length={length} | Upper={use_upper} | Digits={use_digits} | Symbols={use_symbols}")

    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    main()