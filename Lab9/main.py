# represents the amount of books that will be used.
import re
import sys
from random import randint
import json
import os

HOW_MANY_BOOKS = 3
LINE = 128 # How many characters defines a line
PAGE = 64 # how many Lines defines a page
page_number = 0
pages = {}
line_window = {}
line_number = 0
char_window = []

# cleans the text: replaces hyphens with nothing,
# adds space at the end instead of a new line
def clean_line(line):
    return line.strip().replace('-', '') + ' ' #Adding a space instead of a newline.


# *path = this function can accept any number of arguments
def process_books(*paths):
    for path in paths:
        # print(f'Reading {path}')
        read_book(path)
        # print(f"{len(pages)}")

def read_book(file_path):
    global char_window
    with open(file_path, 'r', encoding="utf-8-sig") as fp:
        for line in fp:
            line = clean_line(line)
            # print(line)
            if line.strip():
                for char in line:
                    process_characters(char)
    if len(char_window) > 0:
        add_line()
    if len(line_window) > 0:
        add_line()

def process_characters(char):
    global char_window
    char_window.append(char)
    # prints out each indivual character in a list
    if len(char_window) == LINE:
        add_line()

def add_line():
    global char_window, line_number
    line_number += 1
    process_page("".join(char_window), line_number)
    char_window.clear()

def process_page(line, line_num):
    global line_window, pages, page_number
    line_window[line_num] = line
    if len(line_window) == PAGE:
        add_page()

def add_page():
    global line_window, pages, page_number, line_number
    page_number += 1
    pages[page_number] = dict(line_window) # represents an entire window
    line_window.clear()
    line_number = 0

def generate_code_book():
    global pages
    code_book = {}
    for page, lines in pages.items():
        for num, line in lines.items():
            for pos, char in enumerate(line):
                code_book.setdefault(char, []).append(f"{page}-{num}-{pos}")
    return code_book

def save(file_path, book):
    with open(file_path, "w") as fp:
        #json.dump(book, fp, indent=4)
        json.dump(book, fp)

def load(file_path, *key_books, reverse=False):
    if os.path.exists(file_path):
        with open(file_path, "r") as fp:
            return json.load(fp)
    else:
        process_books(*key_books)
        if reverse:
            save(file_path, pages)
            return pages
        else:
            code_book = generate_code_book()
            save(file_path, code_book)
            return code_book

# encrypt
def encrypt(code_book, message):
    cipher_text =[]
    for char in message:
        index = randint(0, len(code_book[char]) - 1)
        cipher_text.append(code_book[char].pop(index))
    return "-".join(cipher_text)

# decrypt
def decrypt(rev_code_book, ciphertext):
    plaintext = []
    for cc in re.findall(r"\d+-\d+-\d+", ciphertext):
        page, line, char = cc.split("-")
        plaintext.append(rev_code_book[page][line][int(char)])
    return ''.join(plaintext)

# menu
def main_menu():
    print("1). Encrypt \n 2). Decrypt \n 3). Quit")
    return int(input("Make a selection [1,2,3]: "))


def main():
    key_books = ('books/crime-and-punishment.txt', 'books/shakespear.txt', 'books/the-great-gatsby.txt', 'books/war-and-peace.txt')
    code_book_path = 'code_books/book-code.json'
    rev_code_book_path = 'code_books/book-rev.json'
    while True:
        try:
            choice = main_menu()
            match choice:
                case 1:
                    code_book = load(code_book_path, *key_books)
                    message = input("Please enter your secret message: ")
                    print(encrypt(code_book, message))
                    continue;
                case 2:
                    rev_code_book = load(rev_code_book_path, *key_books, reverse=True)
                    message = input("Please enter your cipher text: ")
                    print(decrypt(rev_code_book, message))
                    continue;
                case 3:
                    sys.exit(0)
        except ValueError as ve:
            print("Improper selection.")


if __name__ == '__main__':
    main()

# cb = generate_code_book()
# save("./code_books/super_secret_stuff.json", cb)
# cb = load("./code_books/mega_secret.json", "./books/crime-and-punishment.txt", "./books/shakespear.txt", "./books/war-and-peace.txt", reverse=True)

# print(encrypt())
# print(cb)
# encryption and decryption
#m = input("Type your amazing message:")

# print(
#     encrypt(
#         load('./code_books/super_secret_stuff.json',  "./books/crime-and-punishment.txt", "./books/shakespear.txt", "./books/war-and-peace.txt"), m))


# ct = "56-56-19-132-31-29-73-33-35-39-55-29-117-59-44-100-20-106-8-64-28-3-14-7-76-36-89-118-14-53-109-18-43-122-22-108-138-29-11-37-2-83-94-14-70-59-59-64-111-32-95-20-37-42-8-33-67-6-54-38-35-26-29-22-22-2-44-3-78-126-24-33-21-64-13-116-39-32-68-26-21-45-5-29-39-26-78-70-57-98-67-47-119-30-33-0-71-63-30-140-54-85-139-49-118-83-3-9-104-35-87-3-14-108-109-28-77-85-52-90-16-35-42-19-4-51-66-19-5-32-64-4-18-5-101-95-44-29-11-51-60-104-28-125-10-58-95-9-25-23-78-27-105-59-54-48-46-34-19-113-50-112-9-32-90-114-15-53-32-28-96-61-55-42-115-31-67-79-27-29-79-7-63-12-53-80-4-55-109-21-45-14-26-27-54-35-54-58-123-36-114-93-35-43-97-15-41"
# print(decrypt("./code_books/mega_secret.json", ct))

# print(
#     decrypt(
#         load('./code_books/mega_secret.json',  "./books/crime-and-punishment.txt", "./books/shakespear.txt", "./books/war-and-peace.txt", reverse=True), ct))




