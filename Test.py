from Vigenere import classic_vigenere

def get_user_input():
    message = input("Enter message: ")
    key = input("Enter key (letters only): ").strip()
    
    if not key.isalpha():
        raise ValueError("Key must be alphabetic.")
    return message, key

def run_cipher():
    try:
        message, key = get_user_input()
        encrypted = classic_vigenere(message, key)
        decrypted = classic_vigenere(encrypted, key, "decrypt")
        
        print(f"\nEncrypted: {encrypted}")
        print(f"Decrypted: {decrypted}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run_cipher()