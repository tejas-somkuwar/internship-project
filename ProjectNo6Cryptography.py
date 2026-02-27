import base64
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from Crypto.Hash import SHA256

def show_menu():
    print("\nSelect an option:")
    print("1. AES Encryption (Secure a Message)")
    print("2. AES Decryption (Unlock a Message)")
    print("3. SHA-256 Hashing (Data Integrity)")
    print("4. Exit")
    return input("\nSelect an option (1-4): ")

def aes_encrypt():
    print("\n--- AES Encryption ---")
    plaintext = input("Enter the message to encrypt: ")
    
    key = get_random_bytes(16) 
    cipher = AES.new(key, AES.MODE_CBC)

    ct_bytes = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
   
    print("\nEncryption Successful! Save these details:")
    print(f"Key: {base64.b64encode(key).decode()}")
    print(f"IV: {base64.b64encode(cipher.iv).decode()}")
    print(f"Ciphertext: {base64.b64encode(ct_bytes).decode()}")

def aes_decrypt():
    print("\n--- AES Decryption ---")
    try:
        ct_text = input("Enter Ciphertext: ")
        iv_text = input("Enter IV: ")
        key_text = input("Enter Key: ")

        ciphertext = base64.b64decode(ct_text)
        key = base64.b64decode(key_text)
        iv = base64.b64decode(iv_text)

        cipher = AES.new(key, AES.MODE_CBC, iv)

        decrypted_bytes = unpad(cipher.decrypt(ciphertext), AES.block_size)
        print(f"\nDecrypted Message: {decrypted_bytes.decode()}")
        
    except (ValueError, KeyError) as e:
        print("\nError: Decryption failed. Incorrect Key, IV, or corrupted data.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

def sha_hash():
    print("\n--- SHA-256 Hashing ---")
    text = input("Enter text to hash: ")
    
    hash_obj = SHA256.new(data=text.encode())
    
    print(f"\nText: {text}")
    print(f"SHA-256 Hash: {hash_obj.hexdigest()}")

def main():
    while True:
        choice = show_menu()
        if choice == '1':
            aes_encrypt()
        elif choice == '2':
            aes_decrypt()
        elif choice == '3':
            sha_hash()
        elif choice == '4':
            print("Exiting tool!")
            break
        else:
            print("Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    main()