"""import requests
import hashlib

with open('password.txt','r') as f:
    for line in f:
        username,password=line.strip().split(',')

        password_hash=hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

        response=requests.get(f"https://api.pwnedpasswords.com/range/{password_hash[:5]}") 

        if response.status_code==200:
            hashes=[line.split(',') for line in response.text.splitlines()]

            for h, count in hashes:
                if password_hash[5:]==h:
                    print(f"Password for user {username} has been leaked {count} times.")
                    break
                else:
                    print(f"Could not check password for user {username}.")
"""
import requests
import hashlib

 
with open('password.txt', 'r') as f:
    for line in f:
         
        username, password = line.strip().split(',')

         
        password_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

         
        prefix, suffix = password_hash[:5], password_hash[5:]
        response = requests.get(f"https://api.pwnedpasswords.com/range/{prefix}")

        if response.status_code == 200:
             
            hashes = [entry.split(':') for entry in response.text.splitlines()]
            found = False
            for h, count in hashes:
                if h == suffix:
                    print(f"Password for user '{username}' has been leaked {count.strip()} times.")
                    found = True
                    break
            if not found:
                print(f"Password for user '{username}' has NOT been leaked.")
        else:
            print(f"Error: Unable to check password for user '{username}'. HTTP Status: {response.status_code}")
