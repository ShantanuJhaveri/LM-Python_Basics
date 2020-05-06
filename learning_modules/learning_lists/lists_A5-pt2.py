# part 2
# not allowed to use random.shuffle(), random.sample(),
import random

msg = list(input("ENTER A MESSAGE YOU WOULD LIKE TO ENCRYPT: ").lower())
cypherKey = int(input("ENTER THE CAESAR SHIFT YOU WOULD LIKE FOR YOUR ENCRYPTION (1-25): "))

alpha = list('abcdefghijklmnopqrstuvwxyz')
end = alpha[0:int(cypherKey)]
cypher = alpha[cypherKey:26]
cypher += end
# print(cypher)
# print(msg)
encrypt = ''
decrypt = ''

for i in msg:
    if i.isalpha():
        index = int(alpha.index(i))
        # print(index)
        i = cypher[index]
        # print(i)
    encrypt += i

print("\nENCRYPTING MESSAGE...\n\tENCRYPTED MESSAGE:\t" + str(encrypt))
list(encrypt)

for i in encrypt:
    if i.isalpha():
        index = int(cypher.index(i))
        i = alpha[index]
    decrypt += i

print("\nDECRYPTING MESSAGE...\n\tDECRYPTED MESSAGE:\t" + str(decrypt) + "\n\tORIGINAL MESSAGE:\t" + ''.join(msg))

if decrypt == ''.join(msg):
    print("DECRYPTION SUCCESSFUL")
else:
    print("DECRYPTION ERROR")
