
import hashlib

def crack_hash(hash_to_crack, dictionary_file):
    with open(dictionary_file, 'r') as file:
        for word in file:
            word = word.strip()
            hashed_word = hashlib.sha256(word.encode()).hexdigest()
            if hashed_word == hash_to_crack:
                print(f"Hash cracked! The word is: {word}")
                return
    print("Failed to crack the hash.")

if __name__ == "__main__":
    hash_input = input("Enter SHA-256 hash: ")
    dictionary = input("Enter path to dictionary file: ")
    crack_hash(hash_input, dictionary)
    