# Written by Ivan Infantado Reekie

def print_options():
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")

def encode(password):
    #loops through string and adds 3 and if greater than 9 resets to 0 then counts up
    encoded_pass = ''
    for char in password:
        currentint = int(char)
        if currentint > 6:
            currentint = (currentint + 3) - 10
        else:
            currentint += 3
        encoded_pass = encoded_pass + str(currentint)
    return encoded_pass

def decode(encoded_pass):
    # write decoding function here
    decoded_password = ""
    # for every character in the encoded password
    for char in encoded_pass:
        # convert it into integer
        current_digit = int(char)
        # if it is less than 3 and therefore less than 0 after subtracting 3
        if current_digit < 3:
            current_digit = (current_digit - 3) + 10
        else:
            current_digit -= 3
        # add it into the decoded password string
        decoded_password += str(current_digit)
    return decoded_password

def main():
    program_running = True
    encoded_password = ''
    while(program_running):
        print_options()
        option = int(input("Please enter an option: "))
        match option:
            case 1:
                input_password = input("Please enter your password to encode: ")
                encoded_password = encode(input_password)
                print("Your password has been encoded and stored!\n")
            case 2:
                decoded_password = decode(encoded_password)
                print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}\n")
            case 3:
                program_running = False

if __name__ == '__main__':
    main()