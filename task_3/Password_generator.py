import string
import secrets

def generate_password():
    print("***** PASSWORD GENERATOR *****")
    
    try:
        length = int(input("Enter the desired length of the password: "))
        if length < 4:
            print("Password length should be at least 4 characters for basic complexity.")
            return
    except ValueError:
        print("Please enter a valid integer for the length.")
        return
        
    print("\nSelect complexity options:")
    include_letters = input("Include letters? (yes/no): ").strip().lower() == 'yes'
    include_digits = input("Include numbers? (yes/no): ").strip().lower() == 'yes'
    include_special = input("Include special characters? (yes/no): ").strip().lower() == 'yes'

    # Track selected categories to ensure variety
    pools_selected = []
    if include_letters:
        pools_selected.append(string.ascii_letters)
    if include_digits:
        pools_selected.append(string.digits)
    if include_special:
        pools_selected.append(string.punctuation)
        
    if not pools_selected:
        print("Error: You must choose at least one character type! Defaulting to letters.")
        pools_selected.append(string.ascii_letters)

    # 1. Guarantee at least one character from each selected pool
    password_chars = [secrets.choice(pool) for pool in pools_selected]
    
    # 2. Combine pools for the remaining characters
    full_char_pool = "".join(pools_selected)
    
    # 3. Fill up the rest of the password length
    remaining_length = length - len(password_chars)
    password_chars += [secrets.choice(full_char_pool) for _ in range(remaining_length)]
    
    # 4. Shuffle the list so the guaranteed characters aren't always at the start
    # Since secrets doesn't have a shuffle method, we do it manually with SystemRandom
    secrets.SystemRandom().shuffle(password_chars)
    
    password = "".join(password_chars)
    
    print("\n" + "="*30)
    print(f"Generated Password: {password}")
    print("="*30)

if __name__ == "__main__":
    generate_password()