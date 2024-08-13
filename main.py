# add brute force mode
# add shift amount as input

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

enc_dec = enc_or_dec()

usr_in = input("Enter you phrase: ")


#this function encodes the input
def encode(inp,us_in_lc):
  l0 = []
  for letter in us_in_lc:
    l0.append(letter)

  new_l = []
  for ele in l0:
    #first convert to lower case and then upper case
    if ele.isupper(): # letter is uppercase
      ele = ele.lower()
    # we convert the letter to ascii
    ord_ele = ord(ele)
    # we shift the ascii value of the letter for the shift value
    ord_ele += shift
    ord_ele = chr(ord_ele)
    new_l.append(ord_ele.lower())
  
  #join the list together and return the encoded word
  encoded_word = "".join(new_l)
  print(encoded_word)
  return encoded_word



def decode(inp,us_in_lc):
  print("dec")
    



#decode
if dec:
  decode(enc_dec,usr_in)
else:
  encode(enc_dec,usr_in)


enc_or_dec()