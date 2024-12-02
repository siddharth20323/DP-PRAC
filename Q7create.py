import rsa

 
public_key, private_key = rsa.newkeys(2048)

 
with open('public_key_file.pem', 'wb') as puk:
    puk.write(public_key.save_pkcs1('PEM'))
 
with open('private_key.pem', 'wb') as prk:
    prk.write(private_key.save_pkcs1('PEM'))

print("PRIVATE AND PUBLIC KEYS ARE GENERATED AND SAVED")

 
with open('sample.pdf', 'rb') as f:
    pdf = f.read()
 
signature_file = rsa.sign(pdf, private_key, 'SHA-256')

 
with open('signature_file', 'wb') as sf:
    sf.write(signature_file)

print("DOC IS SIGNED AND SIGNATURE IS SAVED")

 
with open('public_key_file.pem', 'rb') as puk:
    public_key = rsa.PublicKey.load_pkcs1(puk.read())

 
with open('signature_file', 'rb') as sf:
    signature = sf.read()
 
 
try:
    rsa.verify(pdf, signature, public_key)
    print("Signature is valid.")
except rsa.VerificationError:
    print("Signature is not verified (invalid).")
