
def main():
    global option
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    option = input('\nPlease enter an option: ')
    return


def encode(password):

    # Make password a list
    password = list(password)

    # Make each item in list an integer
    # Adds three to each number
    for items in range(0, len(password)):
        password[items] = int(password[items])

    # Checks to see if a number is more than a single digit
        for num in range(1, 4):
            if password[items] == 9:
                password[items] = -1
            password[items] += 1

    # Converts the encoded password back into a string
    password_as_string = ""
    for items in range(0, len(password)):
        password_as_string = password_as_string + str(password[items])

    return password_as_string


#This is the new decode function
def decode(encoded_password):
    decoded_password = ""
    for digit in encoded_password:
        shifted_digit = (int(digit) - 3) % 10
        decoded_password += str(shifted_digit)
    return decoded_password


if __name__ == "__main__":

    # Define variable at program level to remove soft errors (yellow underlines)
    encoded_input = ""
    userinput = ""
    option = ""

    while True:

        main()

        if option == "1":
            userinput = input("Please enter your password to encode: ")
            encoded_input = encode(userinput)
            print("Your password has been encoded and stored!")
            pass

        elif option == "2":
            decoded_input = decode(encoded_input)
            print(f"The encoded password is {encoded_input}, and the original password is {decoded_input}.")
            pass

        elif option == "3":
            break
            
        else:
            print("Invalid input!")

