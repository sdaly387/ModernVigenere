# Vigenere.py

def classic_vigenere(message: str, key: str, mode: str = "encrypt") -> str:
    result = []
    key = key.upper()
    key_index = 0
    
    for char in message:
        if not char.isalpha():
            result.append(char)
            continue
        
        char_code = ord(char.upper()) - ord('A')
        key_shift = ord(key[key_index % len(key)]) - ord('A')
        
        if mode == "decrypt":
            shifted_code = (char_code - key_shift) % 26
        else:
            shifted_code = (char_code + key_shift) % 26
        
        result_char = chr(shifted_code + ord('A'))
        result.append(result_char.lower() if char.islower() else result_char)
        key_index += 1
    
    return ''.join(result)