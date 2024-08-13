dec = False

shift = 3

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
      dec = False
      cor = True
  
  return inp

user_input = enc_or_dec()


#this function encodes the input
def encode(inp):
  #string
  l0 = []
  for letter in inp:
    l0.append(letter)

def decode(inp):
  print("dec")
    



#decode
if dec:
  decode(user_input)
else:
  encode(user_input)


enc_or_dec()