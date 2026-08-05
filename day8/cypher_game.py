
import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if original_text.isdigit():
        output_text = str(original_text)
    else:
        for letter in original_text:
            cipher_text = ""
            if encode_or_decode == "decode":
                for letter in original_text:
                    shifted_position = alphabet.index(letter) - shift_amount
                    shifted_position %= len(alphabet)
                    cipher_text += alphabet[shifted_position]
                    output_text = cipher_text
            else:
                shifted_position = alphabet.index(letter) + shift_amount
                shifted_position %= len(alphabet)
                cipher_text += alphabet[shifted_position]
                output_text = cipher_text
        print(f"Here is the {encode_or_decode}d result: {output_text}")


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

restart = False
while not restart:
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    restart_option = input("type yes to restart or no to end...").lower()
    if restart_option == "no":
        restart = True
    else:
        restart = False
