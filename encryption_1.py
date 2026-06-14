import string

shift = 3

while True:
    print("\n=== CIPHER TERMINAL ===")
    print("1. Encrypt Message")
    print("2. Decrypt Message")
    print("3. Change Shift Value")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '4':
        break

    elif choice == '1':
        message = input("Enter message to encrypt: ")
        encrypted = ""

        for char in message:
            if char.isalpha():

                base = ord('A') if char.isupper() else ord('a')
                shifted = (ord(char) - base + shift) % 26 + base
                encrypted += chr(shifted)

            else:
                encrypted += char

        print("Encrypted message:", encrypted)

    elif choice == '2':
        message = input("Enter message to decrypt: ")
        decrypted = ""

        for char in message:
            if char.isalpha():

                base = ord('A') if char.isupper() else ord('a')
                shifted = (ord(char) - base - shift) % 26 + base
                decrypted += chr(shifted)

            else:
                decrypted += char

        print("Decrypted message:", decrypted)

    elif choice == '3':
        shift = int(input("Enter new shift value: "))
        print("Shift updated to:", shift)

    else:
        print("Invalid option. Try again.")