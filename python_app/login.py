 # MBAN 5502 - Group Project
# Topic 6: Personal Calendar System
# Module 1: Login System

# Function to encrypt text using Caesar cipher

def encrypt_password(password, shift=3):
    encrypted = ""

    for char in password:
        if char.isalpha():
            if char.islower():
                start = ord("a")
            else:
                start = ord("A")

            new_position = (ord(char) - start + shift) % 26
            encrypted += chr(start + new_position)
        else:
            encrypted += char

    return encrypted

def decrypt_password(encrypted_password, shift=3):
    return encrypt_password(encrypted_password, -shift)

# Login System class for the Calendar Project
class LoginSystem:

    def __init__(self, data_manager):
        self.data_manager = data_manager

    
    def login(self):
        users = self.data_manager.get_users()


        # Allow a maximum of 3 login attempts
        for attempt in range(3):
            print("Login attempt:", attempt + 1)

            username = input("Enter your username: ")
            password = input("Enter your password: ")

            encrypted_password = encrypt_password(password)
            decrypted_password = decrypt_password(encrypted_password)

            if username in users and users[username] == decrypted_password:
                print("Login successful! Welcome to your calendar.")
                return True
            else:
                print("Invalid username or password.")

        else:
            print("Maximum login attempts reached. Access denied.")

        return False
