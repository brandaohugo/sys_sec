from Crypto.PublicKey import RSA

key = RSA.generate(2048)
f = open('private.key','w')
f.write(key.exportKey('PEM'))
f.close()

f = open('public.key','w')
f.write(key.publickey().exportKey('PEM'))
f.close()