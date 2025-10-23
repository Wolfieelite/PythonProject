#checks whether the input is a numbers or letters,
# if letters, return false
# (does not check if the value is an int or a string)

def can_be_converted(x):
    try:
        int(x) #this int is needed, error will occure if input is letters. If letters are typed, it will allow the except block to run
        if len(x) > 1 and x[0] == "0":
            print("number cannot have a leading 0")
            return False
        return True
    except ValueError:
        print("You need to enter a number")
        return False

def is_valid_ip(ip):
    parts = ip.split(".")

    # check if the lenth if valid (4 parts)
    if len(parts) != 4:
        print("invalid ip \n There should be 4 parts")
        return False

    for part in parts:
        # print(part)
        if not can_be_converted(part):
            print("invalid ip")
            return False
        
    print("valid ip")
    return True

def decimal_to_binary(n):
    if n == 0:
        return ""
    val = n // 2
    remainder = str(n % 2)
    # return value as a string
    return decimal_to_binary(val) + str(remainder)

def binary_to_decimal(b):
    if b == " ":
        return 0
    #
    n = len(b) - 1
    print("n", n)
    pv = 2 ** n
    d = int(b[0])
    v = pv * d
    print("binary", v)
    return v + binary_to_decimal(b.removeprefix(b[0]))


def is_valid():
    numbers_for_ip = []
    user_number_binary = []

    for _ in range(4):
        user_input = input("Enter a number between 0 and 255 \n \t")
        # user_input = x
        is_number = can_be_converted(user_input) #returns a boolean

        if is_number:
            user_number = int(user_input) #converts the string into an int
            if user_number > 255 or user_number < 0:
                print("please enter a number between 0 and 255 \n \t")
            else:
                numbers_for_ip.append(user_number)
                for num in numbers_for_ip:
                    user_number_binary.append(decimal_to_binary(num))

    ip = ".".join(str(num) for num in numbers_for_ip)
    binary = user_number_binary
    is_ip = is_valid_ip(ip)
    print(f"the ip is {ip} and it is a {is_ip} ip.")
    print(f"user's binary is {binary}")

is_valid()