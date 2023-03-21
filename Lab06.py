def encode(password):
    encoded_password = ""
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password += encoded_digit
    return encoded_password

def decode(password):
    decoded = ""
    for i in password:
        decoded_int = str(int(i) - 3)
        decoded += decoded_int
    return decoded

def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()
        x = int(input("Please enter an option: "))
        if (x == 1):
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
            print()
        if (x == 2):
            print(f"The encoded password is {encoded_password}, and the original password is {decode(encoded_password)}.")
            print()
        if (x == 3):
            break

if __name__ == "__main__":
    main()

