import random

def generate_password():
   
    with open('dictionary.txt') as f:
        words = f.read().splitlines()

    # Selecting 4 random words
    pass_words = random.sample(words, 4)

    # Joining  with a hyphen (-)
    password = '-'.join(pass_words)
    return password

# Example
if __name__ == "__main__":
    password = generate_password()
    print("Generated Password:", password)
