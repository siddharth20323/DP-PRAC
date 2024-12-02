import hashlib
def hash_password(password):  #hashes password to sha -256 algo

    pass_bytes=password.encode('utf-8')

    hash_obj=hashlib.sha256(pass_bytes) #we using sha 256 as mentioned in question

    pass_hash=hash_obj.hexdigest()

    return pass_hash

# input 

password = input("PLS ENTER YOUR PASSWORD...")

# Hash the password
hashed_password = hash_password(password)

# Output the hashed password
print(f"HASHED PASSWORD IS {hashed_password}")