def ErrorHandle():
   open("productkeys.txt", "r")
   if prin.isprintable == False: print( " " + "Is not Printable")
   elif prin.isalnum == False: print( " " + "Is not an alpha-numeric string" )
   elif len(prin) > 16: print(  " " + "Is bad lenght")
   elif len(prin) < 8: print( " " + "Is bad lenght")
   else:
        open("productkeys.txt", "a")
        f.write(prin)
        f.close()
        print( "This Product Key Is Correct!")
import fileinput
import os
import cmd
import base64
f = open("productkeys.txt", "a")
prin = input("Enter Product Key:")
base64_message = prin
base64_bytes = base64_message.encode('ascii')
message_bytes = base64.b64decode(base64_bytes)
prin = message_bytes.decode('ascii')

ErrorHandle()
 
       
    
    