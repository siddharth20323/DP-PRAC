import itertools
import string
def brutef_attk(passowrd):
    chars=string.printable.strip()
    attempts=0

    for length in range(1,len(passowrd)+1):
        for guess in itertools.product(chars,repeat=length):
            attempts+=1

            guess="".join(guess)

            if guess==passowrd:

               return(attempts,guess)
            
    return(attempts,None)
        
password =input("PLS INPUT YOUR PASSWORD: ")
attempts,guess=brutef_attk(password)
if guess:
    print(f"Password cracked in {attempts} attempts. The password is {guess}.") 
else:
    print(f"Password not cracked after {attempts} attempts.")        
    



