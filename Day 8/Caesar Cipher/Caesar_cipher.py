import Art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(text, shift, direction):
    shifted_text = ""

    if direction == "decode":  # shift left.
        shift *= -1
    # when encode, shift right
    for t in text:
        if t in alphabet:  # if there is char in alphabet, shift.
            shifted_text += alphabet[alphabet.index(t) + shift]
        else:  # if there is no char in alphabet, just insert.such of space, number, symbol
            shifted_text += t

    print(f"The {direction}d text is {shifted_text}")


print(Art.logo)
retry = "yes"

while retry == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if shift > 26: #if shift is too long more than alphabet
        shift = shift % 26

    caesar(text, shift, direction)
    retry = input("Type 'yes' if you want to go again, Otherwise type 'no'").lower()

print("Goodbye")

