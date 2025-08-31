alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']





# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.



# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.

#hello ... h... 7  --> s = 2 to the right -- j..9
#alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]  # a-z

def encrypt(org_text, shift_amount):
    ciphered_txt = ""

    for letter in org_text:
        if letter not in alphabet:
            # Skip characters not in alphabet (spaces, punctuation, etc.)
            ciphered_txt += letter
            continue

        original_index = alphabet.index(letter)
        shifted_index = original_index + shift_amount

        # Wrap around if index is larger than alphabet
        if shifted_index >= len(alphabet):
            shifted_index = shifted_index % len(alphabet)
            print(f"⚠️ '{letter}' went past 'z', so its index reset back to {shifted_index} (letter '{alphabet[shifted_index]}').")

        ciphered_txt += alphabet[shifted_index]

    print(f"\nHere is the ENCODED result: {ciphered_txt}")



# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.



direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

while direction != "encode" and direction !="decode":
    direction = input("INVAILD INPUT Type ONLY 'encode' to encrypt, type 'decode' to decrypt:\n").lower()


text = input("Type your message:\n").lower()
wordlist= text.split()
print (wordlist)

while True:
    try:
        shift = int(input("Type the shift number:\n"))
        break   # exit loop if conversion worked
    except ValueError:
        print("INVALID INPUT. Please ONLY enter a number for the shift.")

encrypt(org_text=text,shift_amount=shift)
