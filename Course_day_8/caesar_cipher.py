from art import logo

def cript(plain_text, shift_amount):
    secret=""
    for ch in plain_text:
        secret+=(alphabet[(alphabet.index(ch)+shift_amount)%(len(alphabet))])
    print(f"The encoded text is {secret}")

def decrypt(plain_text, shift_amount):
    encod=""
    for c in plain_text:
        encod+=(alphabet[(alphabet.index(c)-shift_amount)%(len(alphabet))])
    print(f"The encrypted text is {encod}")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)
continue_s = True
while continue_s:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        cript(text, shift)
    else:
        decrypt(text, shift)
    choice = input("Type 'yes' if you want to go again. Otherwise type 'no'\n")
    if choice == 'no':
        continue_s= False
        print("Goodbye")
