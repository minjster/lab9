
# new comment to see in push

def encoder(password):
    encoded_password = ""
    for i in password:
        encoded_digit = str((int(i) + 3) % 10)
        encoded_password += encoded_digit
    return encoded_password


def decoder(encoded_password):
    decoded_password = ""
    for i in encoded_password:
        decoded_digit = str((int(i) - 3) % 10)
        decoded_password += decoded_digit
    return decoded_password


def main():
    while True:
        print("\nMenu\n"
              "-------------\n"
              "1. Encode\n"
              "2. Decode\n"
              "3. Quit\n")

        option = int(input("Please enter an option: "))

        if option == 1:
            password = input("Please enter your password to encode: ")
            encoder(password)
            print("Your password has been encoded and stored!")

        if option == 2:
            print(f"The encoded password is {encoder(password)}, and the original password is {password}.")

        if option == 3:
            break

if __name__ == "__main__":
    main()


