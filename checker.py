import hashlib
import os
import json

# This file will store the hash values of monitored files
HASH_DB = "hash_store.json"


def calculate_file_hash(file_path):
    """
    This function calculates the SHA-256 hash of a given file.
    Hash acts like a digital fingerprint of the file.
    """
    sha256 = hashlib.sha256()

    # Open the file in binary mode
    with open(file_path, "rb") as file:
        # Read the file in chunks to support large files
        while True:
            data = file.read(4096)
            if not data:
                break
            sha256.update(data)

    # Return the final hash value
    return sha256.hexdigest()


def load_hash_database():
    """
    This function loads stored hash values from the JSON file.
    If the file does not exist or is empty/corrupted,
    it safely returns an empty dictionary.
    """
    if not os.path.exists(HASH_DB):
        return {}

    try:
        with open(HASH_DB, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        # Handles empty or corrupted JSON file
        return {}


def save_hash_database(data):
    """
    This function saves updated hash values
    into the JSON database file.
    """
    with open(HASH_DB, "w") as file:
        json.dump(data, file, indent=4)


def check_file_integrity(file_path):
    """
    This is the main function that checks
    whether a file has been modified or not.
    """
    # Check if the file exists
    if not os.path.exists(file_path):
        print("❌ File not found.")
        return

    # Load previously stored hashes
    hash_db = load_hash_database()

    # Calculate the current hash of the file
    current_hash = calculate_file_hash(file_path)

    # If file is being checked for the first time
    if file_path not in hash_db:
        hash_db[file_path] = current_hash
        save_hash_database(hash_db)
        print("✅ File added for monitoring.")
        print("🔐 Hash stored successfully.")

    else:
        # Compare stored hash with current hash
        if hash_db[file_path] == current_hash:
            print("🟢 File is SAFE.")
            print("No changes detected.")
        else:
            print("🔴 WARNING!")
            print("File has been MODIFIED.")
            print("Old Hash:", hash_db[file_path])
            print("New Hash:", current_hash)


# Program execution starts from here
if __name__ == "__main__":
    print("===== FILE INTEGRITY CHECKER =====")

    # Take file path input from the user
    file_path = input("Enter file path: ")

    # Call the integrity check function
    check_file_integrity(file_path)

