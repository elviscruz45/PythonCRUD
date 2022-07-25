# Python3 code to demonstrate
# components, representations
# and variants of uuid1()

import uuid

id = uuid.uuid1()

# Representations of uuid1()
print ("The Representations of uuid1() are : ")
print ("byte Representation : ",end="")
print (repr(id.bytes))
print ("int Representation : ",end="")
print (id.int)

print ("hex Representation : ",end="")
print (id.hex)

print("\n")

# Components of uuid1()
print ("The Components of uuid1() are : ")
print ("Version : ",end="")
print (id.version)

print ("Variant : ",end="")
print (id.variant)

print("\n")

# Fields of uuid1()
print ("The Fields of uuid1() are : ")
print ("Fields : ",end="")
print (id.fields)

print("\n")

# Time Component of uuid1()
print ("The time Component of uuid1() is : ")
print ("Time component : ",end="")
print (id.node)

#en Korea ya tendrias 18 años y 9 meses