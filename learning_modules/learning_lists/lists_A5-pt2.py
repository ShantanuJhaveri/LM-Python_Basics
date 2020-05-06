# part 2
# not allowed to use random.shuffle(), random.sample(),
import random

msg = list(input("ENTER A MESSAGE YOU WOULD LIKE TO ENCRYPT: "))
cypherKey = int(input("ENTER THE CAESAR SHIFT YOU WOULD LIKE FOR YOUR ENCRYPTION (1-25): "))

alpha = list('abcdefghijklmnopqrstuvwxyz')
end = alpha[0:int(cypherKey)]
cypher = alpha[cypherKey:26]
cypher += end
print(cypherKey)
print(msg)

for i in msg:
    index = alpha.index(i)
    print(index)
    replacement = cypher.index(index)
    print(replacement)
