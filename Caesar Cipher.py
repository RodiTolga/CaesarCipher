from art import logo
print(logo)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

continues = True                                               #Used to be able to repeat the code depending on the users choice without having to constantly run the code.

def caesar(start_text, shift_amount, cipher_direction):        #Define the function
    end_text = ""
    if cipher_direction == "decode":                    
            shift_amount *= -1                                 #If user chooses decode, then the shift number must be taken away from end_text
    for char in start_text:                                    
        if char in alphabet:                                   #If statement is used to distinguish if a number or symbol is in the starting input. If a number or symbol is present, then it skips to line 19 for that char
            position = alphabet.index(char)                    #Determines the position of the letter in the alphabet
            new_position = position + shift_amount             #The new letter will be the sum of the position of the letter in the alphabet + the shift amount the user entered
            end_text += alphabet[new_position]                 #The new letter will be added to the initially empty string called_text
        else:
             end_text += char
    print(f"The {cipher_direction}d text is {end_text}")
    
while continues:                                               
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(start_text = text, shift_amount = shift, cipher_direction = direction) 
    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if result =="no":
         continues = False
         print("Goodbye.")
