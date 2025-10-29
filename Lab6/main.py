import sys

letters = 'abcdefghijklmnopqrstuvwxyz'.upper()
def create_vigener_square():
    for y in range(len(letters)):
        # print(" ")
        for x in range(len(letters)):
            shift_letter = (x + y) % len(letters)
            print(letters[shift_letter], end=" | ")
        print(y)
    print("-"*len(letters * 4))

create_vigener_square()

def build_dict():
    list_to_index = {}
    index_to_list = {}

    for index, cypher in enumerate(letters):
        list_to_index[cypher] = index
        index_to_list[index] = cypher
    return list_to_index, index_to_list

def letter_to_index(letter, to_index):
    if letter in to_index:
        return to_index[letter]
    return -1


def index_to_letter(index, to_index):
    if index in to_index:
        return to_index[index]
    return ''

def vigenere_index(key_letter, plain_letter, to_index, to_letter):
    cypher_to_index = (letter_to_index(plain_letter, to_index)) + letter_to_index(key_letter, to_index)
    return index_to_letter(cypher_to_index, to_letter)

def encrypt_vigenere(key, plaintext, to_index, to_letter):
    cypher_to_letter = []
    for i, c in enumerate(plaintext):
        cypher_to_letter.append(vigenere_index(key[i % len(key)], c, to_index, to_letter))
    return ''.join(cypher_to_letter)

def undo_vigenere_index(key_letter, ciphertext_letter, to_index, to_list):
    ptl = (letter_to_index(ciphertext_letter, to_index) - letter_to_index(key_letter, to_list)) % len(to_list) #may be wrong..?
    return index_to_letter(ptl, to_list)

def decrypt_vigenere(key, cipher_text, to_item, to_list):
    ptl = []
    for i, c in enumerate(cipher_text):
        ptl.append(undo_vigenere_index(key[i%len(key)], c, to_item, to_list))
    return "".join(ptl)


def encrypt(key, to_index, to_list, glist):
    message = input("Enter a message to encrypt: ")
    glist.append(encrypt_vigenere(key, message, to_index, to_list))

def decrypt(key, to_index, to_list, glist):
    for item in glist:
        print(decrypt_vigenere(key, item, to_index, to_list))

def dump_decrypt(key, to_index, to_list, glist):
    for item in glist:
        print(key, item, to_index, to_list)

def get_menu_choice(list):
    for i, menu_item in enumerate(list):
        print(f'{i+1}. {menu_item}')

    try:
        choice = int(input("Choose an option: "))
        if 1 <= choice <= len(list):
            return choice - 1
    except ValueError:
        print("Invalid choice")

    return None

key = "DAVINCI"
glist = []
menu = ["Encrypt", "Decrypt", "Dump Encrypted Text", "quit"]
functions = [encrypt, decrypt, dump_decrypt, sys.exit]
massage = "THE EAGLE HAS LANDED"

list_to_index, index_to_list = build_dict()
cypher_text = encrypt_vigenere(key, massage, list_to_index, index_to_list)
print(cypher_text)

 # for y in range(num_of_rows):
    #     if y == 0:
    #         for i in range(num_of_rows):
    #             print("~~~", end= "|")
    #     for x in range(num_of_rows):
    #         letters = chr(start_of_unicode + (x + y) % num_of_rows)
    #         print(letters, end="  |  ")
    #     print("")