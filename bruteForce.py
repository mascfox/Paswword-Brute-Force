import itertools
import string
import hashlib

# Function to hash a password using SHA-256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Brute-force function to guess the password
def brute_force_password(hashed_password, max_length=5):
    characters = string.ascii_letters + string.digits  # Define character set (a-z, A-Z, 0-9)

    # Try all possible combinations of characters up to max_length
    for length in range(1, max_length + 1):
        for guess in itertools.product(characters, repeat=length):
            guess = ''.join(guess)
            guess_hashed = hash_password(guess)
            
            print(f"Trying password: {guess}")  # Display current guess

            if guess_hashed == hashed_password:
                print(f"Password found: {guess}")
                return guess
    
    print("Password not found within the given max length.")
    return None

# Menu-driven system for choosing the task
def main_menu():
    while True:
        print("\nMenu:")
        print("1. Input a SHA-256 hash to brute-force.")
        print("2. Input a plain-text password (the program will hash and brute-force it).")
        print("3. Exit.")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            # Option 1: Input a SHA-256 hash to brute-force
            hashed_password = input("Enter the SHA-256 hash of the password you want to brute-force: ")
            brute_force_password(hashed_password)
        
        elif choice == '2':
            # Option 2: Input a plain-text password and brute-force it
            plain_password = input("Enter the plain-text password to brute-force(no special characters): ")
            hashed_password = hash_password(plain_password)
            print(f"Hash of the password: {hashed_password}")
            brute_force_password(hashed_password)
        
        elif choice == '3':
            # Option 3: Exit the program
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Invalid choice, please select again.")

# Run the menu
main_menu()