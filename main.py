# TODO
# make sure that the letter go from a-z and don't include other ascii characters

from math import floor


def brute_force(user_input_local):
  print("brute force mode")

  l0 = []
  for letter in user_input_local:
    l0.append(letter)
  

  # this goes trough the whole english alphabet
  for shift in range(1,24):
    new_l = []
    for ele in l0:
      ord_ele = ord(ele)
      ord_ele -= shift
      ord_ele = chr(ord_ele)
      new_l.append(ord_ele)
    print(f'{shift}: {"".join(new_l)} \n')
    

usr_phrase = input("Enter you phrase: ")
shift = floor(int(input("Enter the shift amount: ")))

# returns if the function should encode or decode
def enc_or_dec():
  while True:
    inp = input("\"enc\" to encode, \"dec\" to decode, brute to brute force: ")
    if inp == "dec" or inp == "enc" or inp == "brute":
      return inp
    else:
      print("Incorrect input. \n")
  
user_input = enc_or_dec()
  
def encode(user_input_local):
  global user_input
  global shift
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



if user_input == "enc" or user_input == "dec":
  encode(usr_phrase)
elif user_input == "brute":
  brute_force(usr_phrase)
else:
  print("something went wrong")