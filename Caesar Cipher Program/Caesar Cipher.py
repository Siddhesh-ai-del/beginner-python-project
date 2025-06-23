def main():
    # Logo Art for Caesar Cipher Program (just for fun!)
    logo = """           
     ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
    a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
    8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
    "8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
     `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
                88             88                                 
               ""             88                                 
                              88                                 
     ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
    a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
    8b         88 88       d8 88       88 8PP""""""" 88          
    "8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
     `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
                  88                                             
                  88           
    """

    print(logo)

    # Alphabet list used for Caesar cipher shifting
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    # Caesar Cipher Function (works for both encoding and decoding)
    def caesar(original_text, shift_amount, encode_or_decode):
        output_text = ""

        # Flip shift direction for decoding
        if encode_or_decode == "decode":
            shift_amount *= -1

        # Loop through each letter in the original message
        for letter in original_text:

            # If character is not in the alphabet (e.g., space or symbol), keep it unchanged
            if letter not in alphabet:
                output_text += letter
            else:
                # Find new position by shifting
                shifted_position = alphabet.index(letter) + shift_amount
                # Wrap around using modulus if shift goes beyond 'z'
                shifted_position %= len(alphabet)
                # Add shifted character to final output
                output_text += alphabet[shifted_position]

        # Show final result
        print(f"Here is the {encode_or_decode}d result: {output_text}")

    # Start the program loop
    should_continue = True

    while should_continue:
        # Ask user for direction
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        # Get the message
        text = input("Type your message:\n").lower()
        # Get the shift number
        shift = int(input("Type the shift number:\n"))

        # Call Caesar function
        caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

        # Ask if the user wants to restart
        restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
        if restart == "no":
            should_continue = False
            print("Goodbye")

    
if __name__ == '__main__':
    main()