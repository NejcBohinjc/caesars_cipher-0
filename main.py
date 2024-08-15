# TODO
# add brute force mode
# add shift amount as input

from math import floor

shift = floor(int(input("Enter the shift amount: ")))
usr_in = input("Enter you phrase: ")

# returns if the function should encode or decode
def enc_or_dec():
  while True:
    inp = input(" \"enc\" to encode, \"dec\" to decode: ")
    if inp == "dec" or inp == "enc" or inp == "brute":
      return inp
    else:
      print("Incorrect input. \n")
  
user_input = enc_or_dec()
  
def encode(user_input_local):
  global user_input
  l0 = []
  for letter in user_input_local:
    l0.append(letter)

  new_l = []
  for ele in l0:
    # we convert the letter to ascii
    ord_ele = ord(ele)
    # we shift the ascii value of the letter for the shift value
    #decode
    if user_input == "dec": 
      ord_ele -= shift
    #encode
    elif user_input == "enc":
      ord_ele += shift

    ord_ele = chr(ord_ele)
    new_l.append(ord_ele)
  
  #join the list together and return the encoded word
  encoded_word = "".join(new_l)
  print(encoded_word)
  return encoded_word


encode(usr_in)