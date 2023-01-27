import random

master = "Marlon"
def hash_djb2(s):                                                                                                                                
    my_hash = 5381
    for x in s:
        my_hash = (( my_hash << 5) + my_hash) + ord(x)
    return my_hash & 0xFFFFFFFF


print(" Your hash code for the name \'Marlon'\ is ")

my_hash = ''
for c in master:
    my_hash += hex(hash_djb2(c))

print("  hash : ", my_hash)


print(" Your hash code for the name \'Fabio Akita'\ is ")

master = 'Fabio Akita'
my_hash = ''
my_hash = hex(hash_djb2(master))
print("  hash : ", my_hash)



