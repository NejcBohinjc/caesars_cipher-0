dec = False

# decides to decode or encode
def enc_or_dec():
  cor = False #checks if the input was correct
  
  # this checks if the user chooses to decode or encode

  while cor == False:
    inp = input(" \"enc\" to encode, \"dec\" to decode: ")
    if inp == "dec":
      dec = True # decode
      cor = True
    elif inp != "enc":
      print("Incorrect input. \n")
    else:
      cor = True



enc_or_dec()