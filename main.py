from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open("key.crt", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("key.crt", "rb").read()

def encrypt(filename, key, file2):
    """
    Given a filename (str) and key (bytes), it encrypts the file and write it
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read all file data
        file_data = file.read()
    # encrypt data
    encrypted_data = f.encrypt(file_data)
    # write the encrypted file
    with open(file2, "ab") as file:
        file.write(encrypted_data)
    print(encrypted_data)

def decrypt(filename, key, file2):
    f = Fernet(key)
    with open(filename, "rb") as file, open(file2, "wb") as out:
        content = file.read()
        # Find the last JPEG EOI marker (0xFFD9). Some JPEGs can contain
        # the byte sequence earlier, so use rfind to get the final marker.
        marker = bytes.fromhex('FFD9')
        offset = content.rfind(marker)
        if offset == -1:
            # No marker found — assume the file is just the encrypted token
            encrypted_data = content
        else:
            # Encrypted payload should be everything after the final EOI
            encrypted_data = content[offset+2:]
        # Clean common accidental whitespace/newlines
        encrypted_data = encrypted_data.strip()
        # If multiple tokens were appended we may have several Fernet tokens
        # concatenated. Fernet tokens produced by this script start with
        # the ASCII prefix 'gAAAA'. Prefer the last token (most-recent)
        # so that repeated appends decrypt correctly.
        token_prefix = b'gAAAA'
        idx = encrypted_data.rfind(token_prefix)
        if idx != -1:
            encrypted_data = encrypted_data[idx:]
        # decrypt data
        try:
            decrypted_data = f.decrypt(encrypted_data)
        except Exception as exc:
            # Surface a clearer error for common failure modes
            raise type(exc)(
                "Failed to decrypt data — the token may be corrupted or the wrong key was used."
            ) from exc
        # write the original file
        out.write(decrypted_data)
        print(decrypted_data)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Simple File Encryptor Script")
    parser.add_argument("file", help="File to encrypt/decrypt")
    parser.add_argument("file2", help="File to save content")
    parser.add_argument("-g", "--generate-key", dest="generate_key", action="store_true",
                        help="Whether to generate a new key or use existing")
    parser.add_argument("-e", "--encrypt", action="store_true",
                        help="Whether to encrypt the file, only -e or -d can be specified.")
    parser.add_argument("-d", "--decrypt", action="store_true",
                        help="Whether to decrypt the file, only -e or -d can be specified.")

    args = parser.parse_args()
    file = args.file
    file2 = args.file2
    generate_key = args.generate_key

    if generate_key:
        write_key()
    # load the key
    key = load_key()

    encrypt_ = args.encrypt
    decrypt_ = args.decrypt

    if encrypt_ and decrypt_:
        raise TypeError("Please specify whether you want to encrypt the file or decrypt it.")
    elif encrypt_:
        # ensure the output file for encryption ends with .jpg
        if not file2.lower().endswith('.jpg'):
            raise TypeError("When encrypting the output file (file2) must end with .jpg")
        encrypt(file, key, file2)
    elif decrypt_:
        # ensure the input file for decryption is a .jpg
        if not file.lower().endswith('.jpg'):
            raise TypeError("When decrypting the input file (file) must end with .jpg")
        decrypt(file, key, file2)
    else:
        raise TypeError("Please specify whether you want to encrypt the file or decrypt it.")
