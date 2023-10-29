alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
            'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#Import and print the logo from art.py when the program starts.
from art import logo
print(logo)

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1

  for char in start_text:
    #keep the number/symbol/space when the text is encoded/decoded
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"Here's the {cipher_direction}d result: {end_text}")

should_end = False
#While loop that continues to execute the program if the user types 'yes'.
while not should_end:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  #If the user enters a shift that is greater than the number of letters in the alphabet
  #modulus the shift amount by the total number of letter in the alphabet until it fits in 
  shift = shift % 26

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  #Ask the user if they want to restart the cipher program,
  #if they type 'yes' then the program will restart until they type no.
  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_end = True
    print("Goodbye")
    


